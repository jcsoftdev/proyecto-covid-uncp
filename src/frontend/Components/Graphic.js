import React, { useRef, useEffect } from "react";

import Chart from 'chart.js'

const Graphic = () => {
  const graphic = useRef();

  useEffect(() => {
    const ctx = graphic.current.getContext("2d");
    const myChart = new Chart(ctx, {
      type: "pie",
      data: {
        labels: ["s","j"],
        datasets: [
          {
            label: "algo",
            data: [100, 97],
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },
    });
    return () => {};
  }, []);

  return <div className="graphic" style={{width:"100%"}}>
    <canvas ref={graphic} >

    </canvas>
  </div>;
};

export default Graphic;
