import * as React from "react";
import { useRef, useEffect, useState } from "react";
import MapboxGeocoder from "@mapbox/mapbox-gl-geocoder";
// import '@mapbox/mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css';
import icon from "./assets/img/covid-2.png";

import mapboxgl from "mapbox-gl";
const TOKEN =
  "pk.eyJ1IjoiamNzb2Z0aWEiLCJhIjoiY2s3cjBsbzk5MDFvcTNlbXBpeHVhN3B4dSJ9.e8U2_Nao4uub_Qa7gtSoIA";
import "./assets/styles/Map.scss";

function renderMap(map, data) {
  map.on("load", function () {
    map.addControl(
      new MapboxGeocoder({
        accessToken: TOKEN,
        mapboxgl: map,
        })
      );
    map.loadImage(icon, (error, image) => {
      console.log(image);
      if (error) throw error;
      map.addImage("icon", image);

      map.addSource("earthquakes", {
        type: "geojson",
        // Point to GeoJSON data. This example visualizes all M1.0+ earthquakes
        // from 12/22/15 to 1/21/16 as logged by USGS' Earthquake hazards program.
        data: data,
        cluster: true,
        clusterMaxZoom: 14, // Max zoom to cluster points on
        clusterRadius: 50, // Radius of each cluster when clustering points (defaults to 50)
      });

      map.addLayer({
        id: "clusters",
        type: "circle",
        source: "earthquakes",
        filter: ["has", "point_count"],
        paint: {
          "circle-color": [
            "step",
            ["get", "point_count"],
            "#51bbd6",
            5,
            "#f1f075",
            50,
            "#f28cb1",
            70,
            "#ca30a1",
            100,
            "#fa0081",
          ],
          "circle-radius": [
            "step",
            ["get", "point_count"],
            25,
            45,
            50,
            60,
            25,
          ],
        },
      });

      map.addLayer({
        id: "cluster-count",
        type: "symbol",
        source: "earthquakes",
        filter: ["has", "point_count"],
        layout: {
          "text-field": "{point_count_abbreviated}",
          "text-font": ["DIN Offc Pro Medium", "Arial Unicode MS Bold"],
          "text-size": 16,
        },
        // icon: icon,
        // title: "Hola"
      });

      map.addLayer({
        id: "unclustered-point",
        type: "symbol",
        source: "earthquakes",
        filter: ["!", ["has", "point_count"]],
        layout: {
          "icon-image": "icon",
          "icon-size": 0.075,
          "text-field": ["get", "title"],
          "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
          "text-offset": [0, 1.25],
          "text-anchor": "top",
        },
      });
    });

    // Add a new source from our GeoJSON data and
    // set the 'cluster' option to true. GL-JS will
    // add the point_count property to your source data.

    // inspect a cluster on click
    map.on("click", "clusters", function (e) {
      var features = map.queryRenderedFeatures(e.point, {
        layers: ["clusters"],
      });
      var clusterId = features[0].properties.cluster_id;
      map
        .getSource("earthquakes")
        .getClusterExpansionZoom(clusterId, function (err, zoom) {
          if (err) return;

          map.easeTo({
            center: features[0].geometry.coordinates,
            zoom: zoom,
          });
        });
    });

    // When a click event occurs on a feature in
    // the unclustered-point layer, open a popup at
    // the location of the feature, with
    // description HTML from its properties.
    map.on("click", "unclustered-point", function (e) {
      const coordinates = e.features[0].geometry.coordinates;
      const province = e.features[0].properties.nombre;
      const cantidad = e.features[0].properties.cantidad;

      // Ensure that if the map is zoomed out such that
      // multiple copies of the feature are visible, the
      // popup appears over the copy being pointed to.
      // while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
      //   coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
      // }

      new mapboxgl.Popup()
        .setLngLat(coordinates)
        .setHTML(
          `<p style="font-weight: 600;">PROVINCIA: ${province} </br>
                    CONTAGIADOS: <span style="color:var(--bright-red)">${cantidad}</span><p/>`
        )
        .addTo(map);
    });

    map.on("mouseenter", "clusters", function () {
      map.getCanvas().style.cursor = "pointer";
    });
    map.on("mouseenter", "unclustered-point", function () {
      map.getCanvas().style.cursor = "pointer";
    });
    map.on("mouseleave", "unclustered-point", function () {
      map.getCanvas().style.cursor = "";
    });
    map.on("mouseleave", "clusters", function () {
      map.getCanvas().style.cursor = "";
    });
  });
}

function Mapa() {
  const mapRef = useRef();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [markers, setMarkers] = useState([]);

  useEffect(() => {
    mapboxgl.accessToken = TOKEN;
    // setMap()

    if (!loading) {
      const miMapa = new mapboxgl.Map({
        container: mapRef.current,
        style: "mapbox://styles/mapbox/streets-v11",
        // style: 'mapbox://styles/mapbox/dark-v10',
        center: [-75.015152, -9.189967], // starting position [lng, lat]
        zoom: 4,
      });
      console.log(markers);
      renderMap(miMapa, markers);
      // markers.map((item, index) => {

      //   const popup = new mapboxgl.Popup({ offset: 25 }).setText(
      //     `${item.nombre}: ${item.cantidad} infectados`
      //     );
      //     // create DOM element for the marker
      //     // const el = document.createElement('div');
      //     // create the marker
      //     new mapboxgl.Marker(  )
      //     .setLngLat([item.location.lng, item.location.lat])
      //     .setPopup(popup) // sets a popup on this marker
      //     .addTo(miMapa);
      //   })
    }
  }, [loading]);

  useEffect(() => {
    const getData = async () => {
      try {
        const res = await fetch("./pronvince_ubication/", {
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
        });
        const data = await res.json();
        // console.log(data)
        setMarkers(data);
        setLoading(false);
      } catch (error) {
        setLoading(false);
        setError(error);
      }
    };
    getData();
  }, []);

  // useEffect(() => {

  // }, [markers]);

  if (loading) {
    return <h1 className="load">Loading</h1>;
  }
  if (error) {
    console.log(error);
    return <p className="err">there is an error {error.message}</p>;
  }
  return <div className="map" ref={mapRef}></div>;
}

export default Mapa;
