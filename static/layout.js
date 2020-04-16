$(document).ready(function(){
	$("#searchstr").keyup(function(event){
		if (event.keyCode==13) {
			searchval = $("#searchstr").val(); 
    		location.href = "/search/" + searchval; 
		}
	})

    $("#submitbtn").click(function(){
    	searchval = $("#searchstr").val(); 
    	location.href = "/search/" + searchval; 
	})
})