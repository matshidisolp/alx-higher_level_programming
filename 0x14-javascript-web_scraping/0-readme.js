#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-readme.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
