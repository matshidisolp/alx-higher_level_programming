// Fetches the character name from this URL: 
// https://swapi-api.alx-tools.com/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character, using JQuery API

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, statusCode) => {
  $('#character').text(data.name);
});
