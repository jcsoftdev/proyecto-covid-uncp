import React, { useEffect, useState } from "react";
import "./assets/styles/App.css";
import TopCard from "./TopCard";
import Mapa from "./Mapa";
import Overview from "./Overview";
import Graphic from "./Components/Graphic";

function App() {
  const [department, setDepartment] = useState([]);
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const getData = async () => {
      const res = await fetch("./department", {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      });
      // console.log(res)
      const data = await res.json();
      // console.log(data)
      setDepartment(data.data);
      setLoading(false)
    };
    getData();
    return () => {
      // cleanup
    };
  }, []);
  if (loading) {
    return (
      <h1 className="load">"Cargando"</h1>
    )
  }
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
                <label className="switch" htmlFor="checkbox"></label>
              </div>
            </div>
          </div>
        </header>

        <section className="top-cards">
          <div className="wrapper">
            <div className="grid">
              <TopCard />
              <TopCard />
              <TopCard />
            </div>
          </div>
        </section>

        <div className="mapa">
          <Mapa />
        </div>
          <Graphic departments={department}/>

        <div className="overview">
          <div className="wrapper">
            <h2>DEPARTAMENTOS AFECTADOS </h2>
            <div className="grid">
              {department.map((item) => {
                // console.log(item)
                return (
                  <Overview
                    key={item.DEPARTAMENTO}
                    DEPARTAMENTO={item.DEPARTAMENTO}
                    CANTIDAD={item.CANTIDAD}
                  />
                );
              })}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
