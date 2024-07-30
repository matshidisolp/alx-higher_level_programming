#!/usr/bin/node
// Prints the number of movies with “Wedge Antilles” present

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;

    films.forEach(film => {
      if (film.characters.some(character => character.includes(characterId))) {
        count++;
      }
    });

    console.log(count);
  } catch (err) {
    console.error('Error parsing JSON:', err);
  }
});
