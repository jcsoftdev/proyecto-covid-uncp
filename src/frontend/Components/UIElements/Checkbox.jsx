import React, { useRef, useState } from "react";


const CheckBox = ({setChecked, checked }) => {
  const [isChecked, setIsChecked] = useState(checked);
  const checkboxRef = useRef();

  const handleChecked = (e) => {
    const value = e.target.checked;
    setIsChecked(value);
    setChecked(value);
  };

  return (
    <div className="dark-mode">
      <p className="dark-mode-title">Dark Mode</p>
      <input
        type="checkbox"
        className="checkbox"
        ref={checkboxRef}
        checked={isChecked}
        onChange={handleChecked}
        type="checkbox"
        id="switch"
      />
      <label className="switch" htmlFor="switch"></label>
    </div>
    // <div className="checkbox">
    //   <span className="checkbox__text" >{message||`¿Ha donado previamente?`}</span>
    //   <input
    //     ref={checkboxRef}
    //     checked={isChecked}
    //     onChange={handleChecked}
    //     className="checkbox__input"
    //     type="checkbox"
    //     id="switch"
    //   />
    //   <label className="checkbox__label" htmlFor="switch" />
    // </div>
  );
};

export default CheckBox;
