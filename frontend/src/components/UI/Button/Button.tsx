import React from 'react';
import { ButtonPropsType } from './ButtonTypes';
import styles from './Button.module.scss'
import cn from 'classnames'

const Button = ({btnType='fill_purple', size='sm', squared=false, children, myClass, noWrap=false, ...props}: ButtonPropsType) => {
  return (
    <button 
      {...props}
      className={
        cn(styles.btn, styles[btnType], styles[size], squared && styles.squared, myClass, noWrap && styles.nowrap)
      }>{children}</button>
  );
};

export default Button;