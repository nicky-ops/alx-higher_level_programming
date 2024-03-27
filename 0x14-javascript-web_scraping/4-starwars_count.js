#!/usr/bin/node
const request = require('request');
const requestURL = process.argv[2];
request.get(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movieData = JSON.parse(body);
    let count = 0;
    for (const film of movieData.results) {
      for (character of movieData.results[0].characters) {
        if (character === "https://swapi-api.alx-tools.com/api/people/18/") {
        count += 1;
       }
      }
    }
    console.log(count);
  }
});
