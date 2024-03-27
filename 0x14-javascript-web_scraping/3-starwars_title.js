#!/usr/bin/node
const request = require('request');
const requestID = process.argv[2];
const requestURL = `https://swapi-api.alx-tools.com/api/films/${requestID}`;
request.get(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
