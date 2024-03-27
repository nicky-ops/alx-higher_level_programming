#!/usr/bin/node
const request = require('request');
const requestHTTP = process.argv[2];
request.get(requestHTTP, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
