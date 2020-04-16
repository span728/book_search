var display_topics = function() {
	$("#topicsrow").empty();
	$("#topicsrow").append("<span class=\"mediumfont\">Topics:  </span>");
	for (var key in topics) {
		if (topics[key] == true) {
			var topicblob = $("<span class=\"topicblob\" id=\"" + key + "\">" + key + " <span class=\"xfordelete\">X</span></span>");
			$("#topicsrow").append(topicblob);
		}
		if (topics[key] == false) {
			var undoblob = $("<span class=\"undodelete\" id=\"" + key + "\">undo delete</span>"); 
			$("#topicsrow").append(undoblob);
		}
		
	}

	$(".xfordelete").click(function(){
		var topictodelete = $(this).parent().attr('id'); 
		var dict = {
			"id": b_id,
			"topictodelete": topictodelete
		}
		delete_topic(dict); 
	})

	$(".undodelete").click(function(){
		var topictosave = $(this).attr('id'); 
		var dict = {
			"id": b_id,
			"topictosave": topictosave
		}
		undelete_topic(dict); 
	})
}

var activate_all_handles = function() {
	$("#editfansbtn").click(function(){
		// swap out edit bar 
		$("#fans").empty(); 
		var editbar = $("<span class=\"mediumfont\">Number of Fans:</span><textarea class=\"mywidth\" id=\"editfanstxt\" rows=1></textarea><button class=\"btn btn-dark left-space\" id=\"submitfansbtn\">Submit</button><button class=\"btn btn-danger left-space\" id=\"discardfansbtn\">Discard changes</button>");
		$("#fans").append(editbar); 
		$("#editfanstxt").append(num_fans); 

		// add handlers 
		$("#submitfansbtn").click(function(){
			new_num = $("#editfanstxt").val(); 
			dict = create_entry(b_id, new_num); 
			save_num_changes(dict); 
		})

		$("#discardfansbtn").click(function(){
			$("#fans").empty(); 
			var viewbar = $("<span class=\"mediumfont\">Number of Fans: " +  num_fans + "</span><button class=\"btn btn-dark left-space\" id=\"editfansbtn\">edit</button>"); 
			$("#fans").append(viewbar); 
			activate_all_handles();
		})
	});

	$("#editsumbtn").click(function(){
		// swap out edit bar 
		$("#sum").empty(); 
		var editbar = $("<span class=\"mediumfont\">Summary: </span><br><textarea id=\"editsumtxt\" rows=10></textarea><br><button class=\"btn btn-dark\" id=\"submitsumbtn\">Submit</button><button class=\"btn btn-danger left-space\" id=\"discardsumbtn\">Discard changes</button>"); 
		$("#sum").append(editbar); 
		$("#editsumtxt").append(summary); 

		// add handlers
		$("#submitsumbtn").click(function(){
			new_sum = $("#editsumtxt").val(); 
			dict = create_entry(b_id, new_sum); 
			save_summary_changes(dict);
		})

		$("#discardsumbtn").click(function(){
			$("#sum").empty(); 
			var viewbar = $("<span class=\"mediumfont\">Summary: </span><button class=\"btn btn-dark left-space\" id=\"editsumbtn\">edit</button><br>"); 
			$("#sum").append(viewbar); 
			$("#sum").append(summary); 
			activate_all_handles();
		})
	});

}

var delete_topic = function(dict) {
	$.ajax({
        type: "POST",
        url: "/delete_topic",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(dict),
        success: function(result){
            var topics_updated = result["topics"]
            topics = topics_updated
            display_topics()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var undelete_topic = function(dict) {
	$.ajax({
        type: "POST",
        url: "/undelete_topic",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(dict),
        success: function(result){
            var topics_updated = result["topics"]
            topics = topics_updated
            display_topics()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var save_num_changes = function(data) {
	$.ajax({
        type: "POST",
        url: "/update_num",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result){
        	var num_fans_updated = result["num_fans"]
        	num_fans = num_fans_updated
        	$("#fans").empty()
			var viewbar = $("<span class=\"mediumfont\">Number of Fans: " +  num_fans + "</span><button class=\"btn btn-dark left-space\" id=\"editfansbtn\">edit</button>") 
			$("#fans").append(viewbar) 
			activate_all_handles()

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var save_summary_changes = function(data) {
	$.ajax({
        type: "POST",
        url: "/update_sum",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result){
        	var summary_updated = result["summary"]
        	summary = summary_updated
        	$("#sum").empty()
			var viewbar = $("<span class=\"mediumfont\">Summary: </span><button class=\"btn btn-dark left-space\" id=\"editsumbtn\">edit</button><br>") 
			$("#sum").append(viewbar) 
			$("#sum").append(summary)
			activate_all_handles()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function create_entry(id, new_val) {
	var dict = {
		"id": id,
		"new_val": new_val
	};

	return dict; 
}


$(document).ready(function(){
	display_topics(); 
	activate_all_handles();

})