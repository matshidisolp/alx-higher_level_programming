/** Fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays 
  the value of hello from that fetch in the HTML tag DIV#hello.

The translation of “hello” must be displayed in the HTML tag DIV#hello
You must use the JQuery API
Your script must work when it is imported from the <head> tag */

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, statusCode) {
  $('#hello').text(data.hello);
});
