const express = require("express");
const app = express();
const port = 5000;

const { getPositives } = require('./api.js')


getPositives()


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
