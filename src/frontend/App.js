import React, { useEffect, useState } from "react";
import "./assets/styles/App.css";
import TopCard from "./TopCard";
import Mapa from "./Mapa";
import Overview from "./Overview";
import Graphic from "./Components/Graphic";
import CheckBox from "./Components/UIElements/Checkbox";
import Loader from './Components/UIElements/Loader'

function App() {
  const [department, setDepartment] = useState([]);
  const [loading, setLoading] = useState(true)

  const [darkMode, setDarkMode] = useState(false)
  const [label, setLabel] = useState([])
  const [data, setData] = useState([])

  const [loadingPredict, setLoadingPredict] = useState(true)
  const [labelPredict, setLabelPredict] = useState([])
  const [dataPredict, setDataPredict] = useState([[],[]])

  useEffect(() => {
    const getData = async () => {
      try {
        const res = await fetch("./department", {
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
        });
        // console.log(res)
        const myData = await res.json();
        
        // department.map((item) => data.push(item.CANTIDAD));
        // console.log(data)
        setDepartment(myData.data);
        myData.data.map((item) => setLabel(label=>[...label, item.DEPARTAMENTO]));
        myData.data.map((item) => setData(data=>[...data, item.CANTIDAD]));
        setLoading(false)
      } catch (error) {
        
      }
    };
    getData();
    return () => {
      // cleanup
    };
  }, []);

  useEffect(() => {
    const getData = async () => {
      const res = await fetch("./predictions/", {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      });
      // console.log(res)
      const data = await res.json();
      
      // department.map((item) => data.push(item.CANTIDAD));
      // console.log(data)
      // setDepartment(data.data);
      const arraymio = [[],[]]
      data.data.map((item) => setLabelPredict(labelPredict=>[...labelPredict, item.fecha]));
      data.data.map((item) => {arraymio[0].push(item.cantidadReal)});
      data.data.map((item) => {arraymio[1].push(item.cantidadPredecida)});
      data.data.map((item) => setDataPredict(arraymio));
      setLoadingPredict(false)
    };
    getData();
    return () => {
      // cleanup
    };
  }, []);

  useEffect(() => {
    if (darkMode) {
      document.body.classList.remove('is-light-mode')
      document.body.classList.add('is-dark-mode')
    } else {
      document.body.classList.remove('is-dark-mode')
      document.body.classList.add('is-light-mode')
    }
  }, [darkMode])
  
  if (loading) {
    return (
      <Loader/>
    )
  }
  
  // console.log(data);
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
              {/* <div className="dark-mode">
                <p className="dark-mode-title">Dark Mode</p>
                <input type="checkbox" className="checkbox" id="checkbox" />
                <label className="switch" htmlFor="checkbox"></label>
              </div> */}
              <CheckBox checked={darkMode} setChecked={setDarkMode}/>
            </div>
          </div>
        </header>

        <section className="top-cards">
          <div className="wrapper">
            <div className="grid">
              <TopCard cantidad={600438} title="Contagiados"/>
              <TopCard cantidad={28124} title="Muertes"/>
              <TopCard cantidad={421877} title="Alta médica"/>
            </div>
          </div>
        </section>

        <div className="container-data">
          <div className="mapa">
            <Mapa />
          </div>

              
            <div className="graphics">
            <Graphic label={label} data={[[data]]} type="bar" title={["Contagiados por departamento"]}/>
            </div>

        </div>

        <div className="container-data" style={{"flexDirection":"column", "textAlign":"center", marginTop:"2em"}}>
          <h1 >Datos de predicciones</h1>
            {
              !loadingPredict && <Graphic label={labelPredict} data={[dataPredict]} type="line" title={["Predicciones", "Datos Reales"]}/>
            }

        </div>

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
        
        <div className="footer">
          <p>Hecho con mucho cariño &#128154;</p>
          <p>
            Desarrollado por JuanCarlos <a target="_blank" href="https://twitter.com/_jcsoftdev">@jcsoftdev</a>
           
          </p>
        </div>
        
        
      </div>
    </div>
  );
}

export default App;
