var express = require('express');
var app = express();
var bodyParser = require('body-parser')
var requets = require('request');

var urlencodeParser = bodyParser.urlencoded({extended: false});

app.get('/:name',(req,res)=>{
  let url = 'https://www.instagram.com/'+ req.params.name +'/';
  requets(url,(error, response, body) => {
    let parten = /(?<="display_url":")[^",]*/gi;
    let link = body.match(parten);
    res.send(JSON.stringify(link));
  });
});

app.post('/single',urlencodeParser,(req,res) =>{
  let url = req.body.url;
  requets(url,(error, response, body) => {
    let parten = /(?<="display_url":")[^",]*/gi;
    let link = body.match(parten);
    res.send(JSON.stringify(link));
  });
});

app.listen(3000);
console.log('Listening to port 3000');
