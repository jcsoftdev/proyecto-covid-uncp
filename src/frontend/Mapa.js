import * as React from "react";
import { useRef, useEffect } from "react";
// import ReactMapGL from "react-map-gl";
// var mapboxgl = require('mapbox-gl/dist/mapbox-gl.js');
import mapboxgl from "mapbox-gl";
const TOKEN =
  "pk.eyJ1IjoiamNzb2Z0aWEiLCJhIjoiY2s3cjBsbzk5MDFvcTNlbXBpeHVhN3B4dSJ9.e8U2_Nao4uub_Qa7gtSoIA";
import './assets/styles/Map.scss'
function Mapa() {

  const map = useRef();

  useEffect(() => {
    mapboxgl.accessToken = TOKEN;
    const mapa = new mapboxgl.Map({
      container: map.current,
      style: "mapbox://styles/mapbox/streets-v11",
      // style: 'mapbox://styles/mapbox/dark-v10',
      center: [-75.015152,-9.189967 ], // starting position [lng, lat]
      zoom: 4
    });
  }, []);

  return (
    <div className="map" ref={map}></div>
  );
}

export default Mapa;
