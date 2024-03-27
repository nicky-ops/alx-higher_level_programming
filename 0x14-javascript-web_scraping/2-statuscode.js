#!/usr/bin/node
const request = require('request');
const requestHTTP = process.argv[2];
request.get(requestHTTP, function (error, response) {
  console.error('error:', error);
  console.log('code: ', response.statusCode);
});
