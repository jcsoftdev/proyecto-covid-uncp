const { spawnSync } = require("child_process");
const { stringify } = require("querystring");

const getData = (param, param2) => {
  // POSIBLE PARAMS 
  // # get_department_province
  // # get_positives require an index 
  // # get_provinces
  
  const positiveDep = param2 ? spawnSync("python3", [
    "./src/server/python/api.py",
    param,
    param2
  ]): spawnSync("python3", [
    "./src/server/python/api.py",
    param
  ]);

  return positiveDep.output[1].toString()
};

async function api(option, option2) {
  try {
    const POSITIVES_DEPARTAMENT = JSON.parse(getData(option,option2));
    console.log("=========JSON=========");
    console.log(POSITIVES_DEPARTAMENT);
    // console.log(POSITIVES_DEPARTAMENT())
    console.log("=======ENd JSON =======");
    return POSITIVES_DEPARTAMENT;
  } catch (error) {
    console.log("======ERROR PARSE JSON =============");
    console.log(error);
    console.log("error al convertir a json");
  }

  // await getPositives()
}

module.exports = { api };
// export default {getPositives}
