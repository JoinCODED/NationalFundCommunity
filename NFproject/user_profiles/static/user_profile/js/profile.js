$('document').ready(function(){
  $("#articles").hide();
  $("#fav-articles").hide();
  $("#events").hide();
});

function show_hide(event) {
  $("#articles").hide();
  $("#profileBlock").hide();
  $("#fav-articles").hide();
  $("#events").hide();
  switch (event.target.id) {
    case 'overview':
      $("#profileBlock").show();
      console.log(event.target.id);
      break;
    case 'Articles':
      $("#articles").show();
      break;
    case 'Favorite_Articles':
      $("#fav-articles").show();
      break;
    case 'Events':
      $("#events").show();
      break;
  }


}
