#!/usr/bin/node
const request = require('request');
const requestHTTP = process.argv[2];
request(requestHTTP, function (error, response, body) {
  console.error('error:', error);
  console.log('code: ', response && response.statusCode);
});
