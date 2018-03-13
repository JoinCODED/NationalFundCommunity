function register() {
  var button = $("#register-button")
alert("Hi")
   // $.get(url).done(function(data){
     $('#likes_count').text(data.like_count)
    if(button.text()==='Register') {
      button.text('unregister');
    } else {
      button.text('Register');
    }
  // });
}
