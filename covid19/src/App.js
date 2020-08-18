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
  <div className="container-top">
    <TopCard className="top"/>  
    <TopCard className="top"/>  
    <TopCard className="top"/>  
    <TopCard className="top"/>  
    
  </div>  
  <div className="container-mapa">
    <Mapa className="mapa-child"/>
  </div>
  <div className="overview-container">
  <Overview/>
  <Overview/>
  <Overview/>
  <Overview/>
  <Overview/>
  <Overview/>
  </div>
</div>

    </div>
  );
}

export default App;
