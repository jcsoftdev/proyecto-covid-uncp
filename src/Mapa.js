import * as React from 'react';
import { useState } from 'react';
import ReactMapGL from 'react-map-gl';
 
const TOKEN =
 "pk.eyJ1IjoiYWJoaWxhc2hhLXNpbmhhIiwiYSI6ImNqdzFwYWN1ajBtOXM0OG1wbHAwdWJlNmwifQ.91s73Dy03voy-wPZEeuV5Q";
 function Mapa() {
 const [viewport, setViewport] = useState({
    width: '100%',
    height: '100%',
 latitude: -9.189967,
 longitude: -75.015152,
 zoom: 8
 });
 return (
 
 <ReactMapGL
 {...viewport}
 onViewportChange={nextViewport => setViewport(nextViewport)}
 mapStyle="mapbox://styles/mapbox/streets-v10"
 mapboxApiAccessToken={TOKEN}
 />
 );
 }
 
 export default Mapa

