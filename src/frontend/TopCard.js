import React from "react";
import "./assets/styles/App.css";

function TopCard({cantidad, title}) {
  return (
    <div className="TopCard">
      <article className="card facebook">
        <p className="card-title">
          <i className="fas fa-procedures icono" />
          Casos confirmados
        </p>
        <p className="card-followers">
          <span className="card-followers-number">{cantidad}</span>
          <span className="card-followers-title">{title}</span>
        </p>
        <p className="card-today">
          {/* <img src="img/icon-up.svg" alt="today" /> */}
          122 Hoy
        </p>
      </article>
    </div>
  );
}

export default TopCard;
