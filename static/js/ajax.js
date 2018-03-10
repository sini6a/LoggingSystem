$(function() {
	$.ajax({
		type: "POST",
		url: "/logs/search/",
		data: {
			'search_text' : $('#search').val(),
			'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
		},
		success: searchSuccess,
		dataType: 'html'
	});
});

$(function() {
	$('#search').keyup(function() {
		
		$.ajax({
			type: "POST",
			url: "/logs/search/",
			data: {
				'search_text' : $('#search').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType: 'html'
		});
	});
});

function searchSuccess(data, textStatus, jqXHR)
{
	$('.logs_index').html(data);
}
