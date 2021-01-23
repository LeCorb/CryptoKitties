	src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"

	
//$(document).ready(function(){
  //    $("button").click(function(){
    //    $("h1").slideUp(function(){
         
function toggleContent(){
	var contentId = document.getElementById("content")

	contentId.style.display == "block" ? 
	contentId.style.display = "none" : 
	contentId.style.display = "block";
};

function constructTimeoutPromise(){
	return new Promise(function(resolve,reject){
		setTimeout(resolve,2000);
	});
}

//BLUEPRINT
constructTimeoutPromise().then(function(){
	console.log("Ready?");
	return constructTimeoutPromise();
	
	
}).then(function(){
	console.log("Steady!");
	return constructTimeoutPromise();
	
	
}).then(function(){
	console.log("Eddy!");
	return constructTimeoutPromise();
	 

}).then(function(){
	console.log("GO!");
	
});