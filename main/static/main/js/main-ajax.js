<script type="text/javascript">
  $(document).ready(function(event){

    $(document).on('click', '#favourite', function(event){
      console.log("i'm clicked");
      event.preventDefault();
      var id = $(this).attr("value");
      var url = '{% url "favourite_unfavourite" %}';
      $.ajax({
        type: 'POST',
        url: url,
        data: {
            'id': id,
            'csrfmiddlewaretoken': '{{ csrf_token }}',
            },
        dataType: 'jsonp',
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
changes