// Updates the text of the <header> element to New Header!!! 
// when the user clicks on DIV#update_header using JQuery API

$('#update_header').bind('click', function () {
  const header = $('header');
  header.text('New Header');
});
