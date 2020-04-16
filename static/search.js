var display_search_items = function(data) {
	$("#searchresults").empty();

	$("#searchresults").append("<span class=\"mediumfont\">Search Results (" + searchval + "): " + data.length + " </span>"); 

	// $("#searchresults").append("<div class=\"row padbox\"></div>"); 

	data.forEach(function(item, index) {
		var record = $("<div class=\"row bookentry\" id=\"" + item["id"] + "\"><a href=\"/view/" + item["id"] + "\">" + item["title"] + " by " + item["author"] + "</a></div>");
		$("#searchresults").append(record); 

	})

	searchvalupper = searchval[0].toUpperCase() + searchval.slice(1); 

	$("a:contains(" + searchval + ")").html(function (_, html) {
        var regex = new RegExp(searchval, 'gi');
        return html.replace(regex, '<span class="highlight">' + searchval + '</span>');
    });

	$("a:contains(" + searchvalupper + ")").html(function (_, html) {
        var regex = new RegExp(searchval, 'gi');
        return html.replace(regex, '<span class="highlight">' + searchvalupper + '</span>');
    });

}

var display_no_results = function() {
	$("#searchresults").empty();

	var message = $("<div class=\"row\" id=\"noresult\">Sorry, no results found for \"" + searchval + "\"!  Please try again.</div>"); 
	$("#searchresults").append(message); 
}

$(document).ready(function(){
    if (data.length == 0) {
        display_no_results();
    }
    else {
         display_search_items(data);
    }
})