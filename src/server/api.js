const {spawnSync} = require('child_process')
const { stringify } = require('querystring')

let positiveDep = spawnSync('python3',['./src/server/python/api.py', "DEPARTAMENTO"])

const positive_dep = positiveDep.output[1].toString()

async function api() {
  const POSITIVES_DEPARTAMENT = () => JSON.parse(positive_dep)
  try {
    console.log("==========String======")
    console.log(positive_dep)
    console.log("==========End String======")
    console.log("=========JSON=========")
    // console.log(POSITIVES_DEPARTAMENT())
    console.log("=======ENd JSON =======")
  } catch (error) {
    console.log('======ERROR PARSE JSON =============')
    console.log(error)
    console.log("error al convertir a json")
  }

  return POSITIVES_DEPARTAMENT()
  // await getPositives()
}

module.exports = { api }
// export default {getPositives}
