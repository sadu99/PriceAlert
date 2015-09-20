$( document ).ready(function() {
    // $(".intro").fadeIn(2000);
    // setTimeout(function(){ $(".overlay").fadeOut(1000); }, 2000);
      $.ajax({
            url: '/tickers',
            type: 'GET',
            success: function(response) {
                console.log(response);
                responses = JSON.parse(response);
                $( "#end-date" ).autocomplete({
			      source: responses
			    });
            },
            error: function(error) {
                console.log(error);
            }
        });
      
 	var indexArray = [];
    $('#submit-button').click(function(event){
        // Stop the form from actually submitting.        
        event.preventDefault();            
        
        // Capture the entered name and put it into the placeholder.
        var endDate = $('#end-date').val();
        var ticker = "testing";
        var start = "testing";
        var end = "testing";

       
        // window.location.href = "/submit?ticker=" + ticker + "&start=" + start + "&end=" + end;
      
    });

    
 
});