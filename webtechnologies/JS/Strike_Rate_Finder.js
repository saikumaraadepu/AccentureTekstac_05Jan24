//Don't change or delete the try/catch block
function displayStrikeRate() {
    try {
        // Get the name, runs and balls using DOM functions
        var name=document.getElementById("name").value;
        var runs=document.getElementById("runs").value;
        var balls=document.getElementById("balls").value;
        
        // Calculate the strike rate ends with 2 decimal digits
        var strikeRate=((runs/balls)*100).toFixed(2);
        var message="Name : "+name+"<br>Runs Scored : "+runs+"<br>Balls Faced : "+balls+"<br>Strike Rate : "+strikeRate;
        
        // Display the message as per the description in div tag with id "result"
        document.getElementById("result").innerHTML=message;
    } catch(err) {
        document.getElementById("result").innerHTML=err;
    }
}