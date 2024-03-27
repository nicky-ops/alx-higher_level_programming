#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const requestURL = process.argv[2];
const filePath = process.argv[3];

request.get(requestURL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
