function register(url)
{
    var button_text = $("#button_text")
    $.get(url).done(function(data){
        button_text.text(data.is_registerd? 'Unregister':'Register')
    });
}