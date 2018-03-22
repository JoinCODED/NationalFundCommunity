function fav(url) {
  var heart = $("#heart")

  $.get(url).done(function(data){
    $('#fans_number').text(data.fans_number)
    if (data.is_authenticated){
    if(heart.hasClass('text-danger')) {
      heart.removeClass('text-danger');
      heart.addClass('text-muted');
    } else {
      heart.removeClass('text-muted');
      heart.addClass('text-danger');
    }
  } else {
    window.location.href = "/login/";
  }

  });
}
