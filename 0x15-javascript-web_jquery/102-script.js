$(document).ready(function() {
  $('#btn_translate').click(function() {
    let langCode = $('#language_code').val();
    let Url = `https://www.fourtonfish.com/hellosalut/hello/${langCode}`;
    
    $.getJSON(Url, function(data) {
      $('#hello').text(data.hello);
    });
  });
});

