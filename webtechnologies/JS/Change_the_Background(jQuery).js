//WRITE YOUR jQUERY CODE HERE
$("#fname").change(function(){
    $("#demo_form").append("<p>You have changed the First name</p>");
});
$("#lname").change(function(){
        $("#demo_form").append("<p>You have changed the Last name</p>");
});
$("input[type='text']").focusin(function(){
    $(this).css("background-color","green");
}).focusout(function(){
    $(this).css("background-color","grey");
});