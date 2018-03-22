function register(url)
{
    var button_text = $("#button_text")
    var remaining_seats = $("#remaining_seats")
    $.get(url).done(function(data){
        if (data.is_authenticated){
        button_text.text(data.is_registerd? 'Unregister':'Register')
        remaining_seats.text (data.remaining_seats)
        }
        else  {
            window.location.href = "/login/";
          }

    });
}

