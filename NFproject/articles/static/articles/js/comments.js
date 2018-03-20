function comment(url) {
    var button = $("#add_comment")
    $.get(url).done(function(data){
        button.text("Added")

    });
}
