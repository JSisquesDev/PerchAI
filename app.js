require('dotenv').config();

const logger = require('./src/util/logger.js');
//const database = require('./src/settings/database.js');
//const database = require('./src/database/models/index.js');

const express = require('express');
const app = express();
const port = process.env.PORT;

var cors = require('cors');

// CORS
app.use(cors());

// Rutas
app.use(require('./src/services/bird-classification/routes.js'));

app.listen(port, () => {
  logger.info(`Server initialized, runnig at port ${port}`);
});
