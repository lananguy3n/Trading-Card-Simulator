//Take the inputs from React
//Send http requests

//const request = require('request');//A library that makes it easy to send HTTP requests

const express = require('express');//another library that does similar to request.
const bodyParser = require('body-parser');
const cors = require('cors');

const broker = express();
const PORT = 3001;

broker.use(cors());
broker.use(bodyParser.json());
broker.use(bodyParser.urlencoded({extended:true}));//A lot of this is tutorial template that I don't fully understand


broker.post('/open', function (request, response) {//The specified
    console.log("SOMETHING HAPPENED") //Send an html request
})

broker.listen(PORT, () => {
    console.log('Broker listening at port ${PORT}')
} ) //port for the card listen

