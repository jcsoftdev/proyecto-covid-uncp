const {exec} = require('child_process')

const getData = async () => {
  return exec('python3 ./src/server/python/main.py', (err, stdout, sterr) => {
    if (err) {
      console.log(err)
      return false
    }
  
    console.log(stdout)
  })
}

const getPositives = async () => {

  await getData()
  exec('python3 ./src/server/python/positivos.py', (err, stdout, sterr) => {
    if (err) {
      console.log(err)
      return false
    }
  
    console.log(stdout)
  })
}



module.exports = {getPositives}
// export default {getPositives}
