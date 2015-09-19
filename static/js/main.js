$( document ).ready(function() {
    // $(".intro").fadeIn(2000);
    // setTimeout(function(){ $(".overlay").fadeOut(1000); }, 2000);

    $('#submit-button').click(function(event){
        // Stop the form from actually submitting.        
        event.preventDefault();            
        
        // Capture the entered name and put it into the placeholder.
        var endDate = $('#end-date').val();
        console.log(endDate);
    });
});