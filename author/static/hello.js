$(document).ready(function(){
    var baseText = null;
    function showPopup(w,h){
    var popUp = document.getElementById("popupcontent");
    popUp.style.top = "200px";
    popUp.style.left = "200px";
    popUp.style.width = w + "px";
    popUp.style.height = h + "px";
    if(baseText == null) baseText = popUp.innerHTML;
    popUp.innerHTML = baseText + "<div id= \"statusbar\"><button onclick=\"hidePopup();\">
    Close window<button></div>";
    var sbar = document.getElementById("statusbar");
    sbar.style.marginTop = (parseInt(h) - 40)+"px";
    popUp.style.visibility="visible";
    }
    function hidePopup(){
     var popUp = document.getElementById("popupcontent");
     popUp.style.visibility="hidden";
    }
});