
import express from 'express'
import cors from 'cors'
import dotenv from 'dotenv'
import webpack from 'webpack'

dotenv.config()

const { ENV, PORT } = process.env

const app = express();

if (ENV === "development") {
  console.log("development config")
  const webpackConfig = require("../../webpack.config")
  const webpackDevMiddleware = require("webpack-dev-middleware")
  const webpackHotMiddleware = require("webpack-hot-middleware")
  const compiler = webpack(webpackConfig)
  const serverConfig = {port: PORT, hot: true}

  app.use(webpackDevMiddleware(compiler, serverConfig))
  app.use(webpackHotMiddleware(compiler))
}

const { api } = require('./api.js')
app.use(cors())

// const data = api()

app.get('/department/',(req, res)=>{

  const getData = async () => {
    try {
      const data  = await api("get_positives","DEPARTAMENTO")
      // console.log(data)
      res.send(data)
    } catch (error) {
      console.log('error', error)
    }
  }
  getData()
})
app.get('/pronvince_ubication/',(req, res)=>{

  const getData = async () => {
    try {
      const data  = await api("get_provinces")
      // console.log(data)
      res.send(data)
    } catch (error) {
      console.log('error', error)
    }
  }
  getData()
})

app.get('/All/',(req, res)=>{

  const getData = async () => {
    try {
      const data  = await api("get_provinces")
      console.log(data)
      res.send(data.data)
    } catch (error) {
      console.log('error', error)
    }
  }
  getData()
})


app.listen(PORT, (err) => {
  if (err) console.log(err)
  else console.log(`Example app listening at http://localhost:${PORT}`);
});
