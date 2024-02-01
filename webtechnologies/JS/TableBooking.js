//Don't change or delete the try/catch block
function displayConfirmationMessage() {
    try {
        //Get the customer name and timing using DOM functions
        var name=document.getElementById("name").value;
        var timings=document.getElementsByName("timing");
        var timing;
        for(var i=0; i<timings.length;i++){
            if (timings[i].checked){
                timing=timings[i].value;
                break;
            }
        }
        
        //Display the output in div with id "result"
        var message="Hi "+name+" your table has been booked between "+timing;
        document.getElementById("result").innerHTML=message;
        
    } catch(err) {
        document.getElementById("result").innerHTML=err;
    }
}