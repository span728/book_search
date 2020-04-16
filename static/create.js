var error_to_screen = function() {
	var record = $("<div class=\"redfont\">Error occurred: unable to add record.  Please try again.  </div>"); 
	$("#newlink").append(record); 
}

var add_book = function(new_entry) {
	$.ajax({
        type: "POST",
        url: "add_book",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(new_entry),
        success: function(result){
            var all_data = result["data"]
            var new_book_entry = result["new_book_entry"]
            data = all_data
            create_link(new_book_entry); 
            $(".bookform").val("");
            $("#booktitle").focus(); 
            $("#w1, #w2, #w3, #w4, #w5, #w6").empty(); 
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
            error_to_screen(); 
        }
    });
}

var create_dict = function(title, author, num_fans, topics, summary, cover) {
	var topicsdict = {};

	topics.forEach(function(item, index){
		console.log(item);
		topicsdict[item]=true;
	})


	var dict = {
		"title": title, 
		"author": author, 
		"num_fans": num_fans, 
		"topics": topicsdict, 
		"summary": summary, 
		"cover": cover
	}; 

	return dict; 
}


var save_book = function() {
	// get all elements
	var title = $("#booktitle").val().trim(); 
	var author = $("#author").val().trim(); 
	var num_fans = $("#num_fans").val().trim(); 
	var topics = $("#topics").val().split(", ");
	var summary = $("#summary").val().trim(); 
	var summary_num_words = summary.split(" "); 
	var cover = $("#cover").val(); 
	var no_error = true; 
	
	if (cover == "") { // url empty
		$("#w6").append("<span class=\"warning\">Cover photo field cannot be empty</span>"); 
		$("#cover").focus();
		no_error = false; 
	}
	if (summary == "") { // summary empty
		$("#w5").append("<span class=\"warning\">Summary field cannot be empty</span>"); 
		$("#summary").focus();
		no_error = false; 
	}
	if (summary != "" && summary_num_words.length <100) { // summary too short
		$("#w5").append("<span class=\"warning\">Summary must be at least 100 words</span>"); 
		$("#summary").focus();
		no_error = false; 
	}
	if (topics == "") { // topics empty
		$("#w4").append("<span class=\"warning\">Topics field cannot be empty</span>"); 
		$("#topics").focus();
		no_error = false; 
	}
	if (num_fans == "") { // num_fans empty
		$("#w3").append("<span class=\"warning\">Number of Fans field cannot be empty</span>"); 
		$("#num_fans").focus();
		no_error = false; 
	}
	if (num_fans != "" && !$.isNumeric(num_fans)) { // num_fans not a number
		$("#w3").append("<span class=\"warning\">Number of Fans field must be a #</span>"); 
		$("#num_fans").focus();
		no_error = false; 
	}
	if (author == "") { // author empty
		$("#w2").append("<span class=\"warning\">Author field cannot be empty</span>"); 
		$("#author").focus();
		no_error = false; 
	}
	if (title == "") { // title empty
		$("#w1").append("<span class=\"warning\">Title field cannot be empty</span>"); 
		$("#booktitle").focus();
		no_error = false; 
	}

	if (no_error) { // ready to add book
		var new_entry = create_dict(title, author, num_fans, topics, summary, cover); 
		add_book(new_entry); 
	}
}


var create_link = function(new_entry) {
	var record = $("<div>New item succesfully created: <a href=\"/view/" + new_entry["id"] + "\">Click here to view</a></div>"); 
	$("#newlink").append(record); 
}


$(document).ready(function(){
	$("#booktitle").focus(); 

	$("#submitnewbk").click(function(){
		$("#newlink").empty(); 
		$("#w1, #w2, #w3, #w4, #w5, #w6").empty(); 
		save_book(); 
	})
})