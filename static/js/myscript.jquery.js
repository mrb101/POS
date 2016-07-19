$(document).ready(function() {
    // http://jsfiddle.net/Mse2L/
    $(.'checked').change(function() {
        if ($(this).hasClass('checkdisplay') && this.checked) $('.todisplay').fadeIn('slow');
        else $('.todisplay').fadeOut('slow')
    });
});

