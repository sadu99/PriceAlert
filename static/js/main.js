$( document ).ready(function() {
    $(".intro").fadeIn(2000);
    setTimeout(function(){ $(".overlay").fadeOut(1000); }, 3000);
      $.ajax({
            url: '/tickers',
            type: 'GET',
            success: function(response) {
                console.log(response);
                responses = JSON.parse(response);
                $( "#index-value" ).autocomplete({
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
        var ticker = $("#index-value").val();
        var start = "2014-01-01";
        var end = endDate;
        window.location.href = "/submit?ticker=" + ticker + "&start=" + start + "&end=" + end;
		// $.ajax({
  //           url: '/submit',
  //           data: {
  //           	ticker: ticker,
  //           	start: start,
  //           	end: end
  //           },
  //           type: 'GET',
  //           success: function(response) {
  //               console.log(response);
  //           },
  //           error: function(error) {
  //               console.log(error);
  //           }
  //       });


       
       
      
    });

    
 
});