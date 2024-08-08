/** Fetches and lists the title for all movies by using this URL: 
https://swapi-api.alx-tools.com/api/films/?format=json
All movie titles must be list in the HTML tag UL#list_movies
You must use the JQuery API
*/

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, statusCode) {
  const list = $('#list_movies');
  $.each(data.results, function (indx, obj) {
    const title = obj.title;
    list.append(`<li>${title}</li>`);
  });
});
