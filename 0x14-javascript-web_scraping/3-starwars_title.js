#!/usr/bin/node

const request = require('request');
const args = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${args[0]}`;

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
