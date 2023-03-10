import React from "react";

export type ButtonPropsType = React.ButtonHTMLAttributes<HTMLButtonElement> & React.ClassAttributes<HTMLButtonElement> & {
  btnType?: string;
  size?: string;
  children: string | React.ReactElement;
  squared?: boolean;
  myClass?: string;
  noWrap?: boolean;
}