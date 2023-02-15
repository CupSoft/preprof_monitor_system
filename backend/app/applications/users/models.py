from typing import Optional

from tortoise import fields
from tortoise.exceptions import DoesNotExist

from app.applications.users.schemas import BaseUserCreate
from app.core.base.base_models import BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin, BaseDBModel
from app.core.auth.utils import password


class User(BaseDBModel, BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin):

    username = fields.CharField(max_length=20, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    password_hash = fields.CharField(max_length=128, null=True)
    last_login = fields.DatetimeField(null=True)
    is_active = fields.BooleanField(default=True)
    is_superuser = fields.BooleanField(default=False)
    resources: fields.ReverseRelation["Resource"]
    reviews: fields.ReverseRelation["Review"]


    def full_name(self) -> str:
        if self.first_name or self.last_name:
            return f"{self.first_name or ''} {self.last_name or ''}".strip()
        return self.username

    @classmethod
    async def get_by_email(cls, email: str) -> Optional["User"]:
        try:
            query = cls.get_or_none(email=email)
            user = await query
            return user
        except DoesNotExist:
            return None

    @classmethod
    async def get_by_username(cls, username: str) -> Optional["User"]:
        try:
            query = cls.get(username=username)
            user = await query
            return user
        except DoesNotExist:
            return None

    @classmethod
    async def create(cls, user: BaseUserCreate) -> "User":
        user_dict = user.dict()
        password_hash = password.get_password_hash(password=user.password)
        model = cls(**user_dict, password_hash=password_hash)
        await model.save()
        return model

    class Meta:
        table = 'users'

    class PydanticMeta:
        computed = ["full_name"]


class Admin(BaseDBModel, BaseCreatedUpdatedAtModelMixin, UUIDDBModelMixin):
    
    user: fields.ForeignKeyRelation['User'] = fields.OneToOneField(
        'models.User', on_delete=fields.CASCADE
    )
    
    class Meta:
        table = 'admins'
        
    