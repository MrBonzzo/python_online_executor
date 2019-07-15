function button_click() {
    $.ajax({
        url: '/launch',
        type: 'POST',
        dataType: "json",
        data: $('form').serialize(),
        success: function(response) {
            if(response['out']) {
            	$('#stdout').html(response['out']);
                $('#stdout').removeClass('inactive-window');
            } else {
            	$('#stdout').html('');
            	$('#stdout').addClass('inactive-window');
            }

            if(response['err']) {
            	$('#error').html(response['err']);
                $('#error').removeClass('inactive-window');
            } else {
            	$('#error').html('');
            	$('#error').addClass('inactive-window');
            }
        }
    });
};
