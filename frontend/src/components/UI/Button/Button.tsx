import React from 'react';
import { ButtonPropsType } from './ButtonTypes';
import styles from './Button.module.scss'
import cn from 'classnames'

const Button = ({btnType='fill_purple', size='sm', squared=false, children, ...props}: ButtonPropsType) => {
  return (
    <button 
      {...props}
      className={
        cn(styles.btn, styles[btnType], styles[size], squared && styles.squared)
      }>{children}</button>
  );
};

export default Button;