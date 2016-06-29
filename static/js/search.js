$(document).ready(function(){

	$('#send-search').click(function(){
		var search = $('#search').val();
		var url = '/portfolio/api/portfolios/?search=' + search;

		$.get(url).done(function(results){
			$('#results').empty();

			$.each(results, function(index, result){
				var html = '<li>Title: '
				html += '<a href="' + result.url + '">' + result.title + '</a>';
				html += '</li>';

				$('#results').html($('#results').html() + html);
			});
		});
	});

	$('#create-post').ajaxForm();

});