import React from 'react';
import './App.css';
import TopCard from './TopCard';
import Mapa from './Mapa';
import Overview from './Overview'


function App() {
  return (
    <div className="App">
      <div>
  <header className="header">
    <div className="wrapper">
      <div className="header-grid">
        <div>
          <h1>CASOS DE CORONA VIRUS EN EL PERÚ</h1>
          <p className="header-total">Casos Actuales: 154 K</p>
        </div>
        <div className="dark-mode">
          <p className="dark-mode-title">Dark Mode</p>
          <input type="checkbox" className="checkbox" id="checkbox" />
          <label className="switch" htmlFor="checkbox">
          </label>
        </div>
      </div>
    </div>
  </header>

 <section className="top-cards">
  <div className="wrapper">
    <div className="grid">
      <TopCard/>
      <TopCard/>
      <TopCard/>
      <TopCard/>
    </div>
  </div>
</section>

<div className="mapa">
<Mapa/>
</div>

<div className="overview">
  <div className="wrapper">
    <h2>DEPARTAMENTOS MÁS AFECTADOS </h2>
    <div className="grid">
      <Overview/>
      <Overview/>
      <Overview/>
      <Overview/>
      <Overview/>
      <Overview/>
      <Overview/>
      <Overview/>
    </div>
  </div>
</div>

 
</div>

    </div>
  );
}

export default App;
