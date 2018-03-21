function comment(url) {
    
    var form = $('#comment-form');

    
    $.ajax({
        url: url,
        data: form.serialize(),
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            
          if (data.form_is_valid) {
            $("#comments_list").html(data.html_comment_list);
            $("#comment-form")[0].reset();
          }
          else {
            alert("Try Again!");
          }
        }
      });
}
