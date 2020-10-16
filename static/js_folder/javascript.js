$(document).ready(function(){

	$('input:file').change(
	    function(){
	        if ($(this).val()) {
	            $('button:submit').attr('disabled',false);
	        } 
	    });

	$("#searchInput").keyup(function(){

		const input = {
	        q: $(this).val() 
	    }

	    $.getJSON('/', input)
	        .done(response => {
	            // fade out the artists_div, then:
	            $('#tableContainer').fadeTo(100, 0).promise().then(() => {
	                // replace the HTML contents
	                $('#tableContainer').html(response['html_passed'])
	                // fade-in the div with new contents
	                $('#tableContainer').fadeTo(100, 1)
	            })
	        })
		});
})







