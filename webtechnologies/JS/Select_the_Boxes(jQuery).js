//WRITE YOUR jQUERY CODE HERE
$("input[type='checkbox']").on("change",function(){
    var total=$("input[type='checkbox']:checked").length;
    if (total===1){
        $("#result").html(total+" box is checked");
    }
    else{
        $("#result").html(total+" boxes are checked");
    }
});