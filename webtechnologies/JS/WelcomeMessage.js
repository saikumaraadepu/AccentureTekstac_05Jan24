//Don't change or delete the try/catch block
function displayWelcomeMessage() {
    try {
        //Get the first name and last name using DOM functions
        var firstname=document.getElementById("fname").value;
        var lastname=document.getElementById("lname").value;

        //Display the output in div with id "result"
        document.getElementById("result").innerHTML="Welcome "+firstname+" "+lastname;
    } catch(err) {
        document.getElementById("result").innerHTML=err;
    }
}