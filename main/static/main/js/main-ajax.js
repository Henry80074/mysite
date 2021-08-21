<script type="text/javascript">
  $(document).ready(function(event){

    $(document).on('click', '#favourite', function(event){
      console.log("i'm clicked");
      event.preventDefault();
      var activity_id = $(this).attr("value");
      var url = '{% url "account:favourite_unfavourite" %}';
      $.ajax({
        type: 'POST',
        url: url,
        data: {
            'activity_id': id,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
        dataType: 'json',
        success: function(response){
        console.log('success', response)
          $('#favourite-section').html(response['form'])
        },
        error: function(response){
          console.log('error', response);
        },
      });
    });
  });
</script>