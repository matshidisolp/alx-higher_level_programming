#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');

const [url, filePath] = process.argv.slice(2);

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
