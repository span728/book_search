var display_recent_entries = function(data, current_id) {
	$("#recententries").empty(); 

	$("#recententries").append("<span class=\"mediumfont\">Browse Books:</span>"); 

    stop = current_id-10; 

    $("#recententries").append("<div class=\"card-columns\">"); 


	data.forEach(function(item, index) {

        if (item["id"]>stop) {
            var record = $("<div class=\"card\" style=\"width: 16rem;\"><a href=\"/view/" + item["id"] + "\">" + "<img class=\"card-img-top\" src=" + item["cover"]+ " alt=\"Cover photo of " + item["title"] + "\"></a><div class=\"card-body\"><h5 class=\"card-title\">" + item["title"] + " by " + item["author"] + "</h5></div></div>"); 
        }
		$(".card-columns").append(record); 
	})

}

$(document).ready(function(){
    display_recent_entries(data, current_id); 
})