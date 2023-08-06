$(document).ready(function() {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function(event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const langCode = $('#language_code').val();
    const Url = `https://www.fourtonfish.com/hellosalut/hello/${langCode}`;

    $.getJSON(apiUrl, function(data) {
      $('#hello').text(data.hello);
    });
  }
});
