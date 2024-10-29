const { faker } = require('@faker-js/faker')
const mysql = require('mysql2')

var connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "ja@973161",
  database: "delta_app",
});
try {
  connection.query("SHOW TABLES", (err, result) => {
    if (err) throw err;
    console.log(result);
  });
} catch (error) {
  console.log(error)
}


function getRandomUser() {
  return {
    id: faker.string.uuid(),
    username: faker.internet.userName(),
    email: faker.internet.email(),
    password: faker.internet.password(),
  };
}
