$(document).ready(function() {
$.ajax({
  url: "https://swapi-api.alx-tools.com/api/films/?format=json",
  dataType: "json",
  success: function(data) {
    $.each(data.results, function(index, movie) {
      $("#list_movies").append("<li><ul/>" + movie.title + "</li></ul>")
    })
  }
  });
});
