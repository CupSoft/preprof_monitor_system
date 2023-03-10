from tortoise import fields

from app.applications.resources.schemas import Status
from app.core.base.base_models import BaseModel
from app.applications.checks.schemas import RequestType, Location


class Check(BaseModel):
    resource_node: fields.ForeignKeyRelation["ResourceNode"] = fields.ForeignKeyField(
        "models.ResourceNode", related_name="checks", to_field="uuid", on_delete=fields.CASCADE
    )
    results: fields.ReverseRelation["CheckResult"]
    expectation = fields.CharField(max_length=255)
    request_type = fields.CharEnumField(RequestType)

    class Meta:
        table = "checks"


class CheckResult(BaseModel):
    parent_check: fields.ForeignKeyRelation["Check"] = fields.ForeignKeyField(
        "models.Check", related_name="results", to_field="uuid", on_delete=fields.CASCADE
    )
    response = fields.CharField(max_length=255)
    status = fields.CharEnumField(Status)
    datetime = fields.DatetimeField(auto_now_add=True)
    location = fields.CharEnumField(Location)

    class Meta:
        table = "check_results"
