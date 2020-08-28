import React from "react";

import '../../assets/styles/Loader.scss'

const Loader = () => {
  return (
    <div className="loader">
      <div className="loading-circle resonance"></div>
      <div className="loading-circle resonance2"></div>
      <div className="loading-circle loaderz">
        <p className="loading-text ldt-1">Loading</p>
        {/*         <p class="loading-text ldt-2">Hang</p>
  <p class="loading-text ldt-3">Tight</p>
  <p class="loading-text ldt-4">One</p>
  <p class="loading-text ldt-5">Sec</p> */}
        <div className="ld-container">
          <div className="ld-circ ld-circ-1" />
          <div className="ld-circ ld-circ-2" />
          <div className="ld-rect ld-rect-1" />
          <div className="ld-rect ld-rect-2" />
          <div className="ld-rect ld-rect-3" />
          <div className="ld-rect ld-rect-4" />
        </div>
        <div className="ld-rot">
          <div className="ld-line ld-rect-5" />
          <div className="ld-line ld-rect-6" />
        </div>
        {/*     <div class="ld-quarters">
    <div class="ld-quarter-circle-1"></div>
    <div class="ld-quarter-circle-2"></div>
    </div> */}
      </div>
    </div>
  );
};

export default Loader;
