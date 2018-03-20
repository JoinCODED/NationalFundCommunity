function comment(url) {
    console.log(url);
    var form = $('#comment-form');

    console.log(form.serialize())
    $.ajax({
        url: url,
        data: form.serialize(),
        type: 'POST',
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            alert("Comment created!");  // <-- This is just a placeholder for now for testing
          }
          else {
            alert("No Comment!");
          }
        }
      });
}
