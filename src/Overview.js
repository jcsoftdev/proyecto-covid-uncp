import React from 'react';
import './App.css';

function Overview() {
  return (
    <div className="TopCard">
<div className="card-small">
  <p className="card-small-views">Lima Metropolitana</p>
  <p className="card-small-icon">
    <img src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Flag_of_Lima.svg/20px-Flag_of_Lima.svg.png" alt />
  </p>
  <p className="card-small-number">222 840</p>
  <p className="card-small-percentage">
    <span>
      <img src="img/icon-up.svg" alt />
      1%
    </span>
  </p>
</div>



    </div>
  );
}

export default Overview;