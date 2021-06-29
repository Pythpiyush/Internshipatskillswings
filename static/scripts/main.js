var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}

function sendOTP()
{
	var emailph = document.getElementById('emailph');
	document.getElementById('form1').style.display='none';
	document.getElementById('form2').style.display='block';
}

function verify()
{
	var emailph = document.getElementById('emailph');
	document.getElementById('form2').style.display='none';
	document.getElementById('form3').style.display='block';
	
}

function coursePage()
{
	var col4 = document.createElement("div");
	col4.addClass("col-sm-4");
	var courses = document.createElement("div");
	courses.addClass("courses");
	col4.appendChild(courses);
	var imgdiv = document.createElement("div");
	var img = document.createElement("img");
	img.addClass("img-fluid");
	img.setAttribute("src","imgpath");
	imgdiv.appendChild(img);
	courses.appendChild(imgdiv);
	
}

function registerNow()
{
	//document.getElementById("loginModal").style.display="none";
	//document.getElementById("registerModal").style.display="block";
	$("#loginModal").modal("hide");
	$("#registerModal").modal("show");
}