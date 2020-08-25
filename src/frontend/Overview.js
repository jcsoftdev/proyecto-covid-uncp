import React from "react";
import "./assets/styles/App.css";

import icon from './assets/img/icon-up.svg'

const Overview = ({DEPARTAMENTO, CANTIDAD}) => {

  // console.log(DEPARTAMENTO)

  return (
    <div className="TopCard">
      <div className="card-small">
        <p className="card-small-views">{DEPARTAMENTO}</p>
        <p className="card-small-icon">
          {/* <img
            src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Flag_of_Lima.svg/20px-Flag_of_Lima.svg.png"
            alt="flag"
          /> */}
        </p>
        <p className="card-small-number">{CANTIDAD} </p>
        <p className="card-small-percentage">
          <span>
            <img src={icon} alt="up icon" />
            1%
          </span>
        </p>
      </div>
    </div>
  );
};

export default Overview;
