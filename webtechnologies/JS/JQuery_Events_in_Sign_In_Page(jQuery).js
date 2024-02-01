//Debug and obtain the result as given in the description
$("#uname").change(function() {
    $("<p>You have changed the Username</p>").appendTo("form");
});

$("#pwd").change(function() {
    $("<p>You have changed the Password</p>").appendTo("form");
});

$("#login").dblclick(function() {
    $("<p>You have double clicked on Sign In</p>").appendTo("form");
});

$("#uname").focusin(function(){
    $(this).css("background-color","green"); 
}).focusout(function(){
    $(this).css("background-color","grey");
});

$("#pwd").focusin(function(){
    $(this).css("background-color","green"); 
}).focusout(function(){
    $(this).css("background-color","grey");
});
