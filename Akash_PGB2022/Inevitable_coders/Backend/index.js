const express = require("express");
const path = require("path");

const { open } = require("sqlite");
const sqlite3 = require("sqlite3");
const app = express();

const dbPath = path.join(__dirname, "assignment.db");
const cors=require("cors")
let db = null;

const initializeDBAndServer = async () => {
  try {
    db = await open({
      filename: dbPath,
      driver: sqlite3.Database,
    });
    app.listen(5000, () => {
      console.log("Server Running at http://localhost:5000/");
    });
  } catch (e) {
    console.log(`DB Error: ${e.message}`);
    process.exit(1);
  }
};

initializeDBAndServer();
app.use(
  cors({
    origin:"*"
  })
)
app.get("/", (request, response) => {
  response.send("Hello World!");
});
app.get("/java/", async (request, response) => {
  const getJavaQuery = `
    SELECT
      *
    FROM
      java;`;
  const javaArray = await db.all(getJavaQuery);
  response.send(javaArray);
});
app.get("/python/", async (request, response) => {
  const getPythonQuery = `
    SELECT
     *
    FROM
      python;`;
  const python = await db.all(getPythonQuery);
  response.send(python);
});
app.get("/javascript/", async (request, response) => {
  const getJavascriptQuery = `
    SELECT
      *
    FROM
    javascript;`;
  const javascript = await db.all(getJavascriptQuery);
  response.send(javascript);
});