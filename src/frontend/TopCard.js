import React from "react";
import "./assets/styles/App.css";

function TopCard() {
  return (
    <div className="TopCard">
      <article className="card facebook">
        <p className="card-title">
          <i className="fas fa-procedures icono" />
          Casos confirmados
        </p>
        <p className="card-followers">
          <span className="card-followers-number">478 K</span>
          <span className="card-followers-title">Contagiados</span>
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
