//Don't change or delete the try/catch block

function display()
{
    // Get the value of ugly component 
   var num=document.getElementById("ugly").value;
   
   // Check if it's a valid input or not.
   if (!num){
       alert("Please, specify an input");
       return;
   }
   if (num<=0){
       alert("Invalid Input");
       return;
   }
   
   // IF valid, invoke checkUglyNumber() function and display the output statement using alert()
   // IF invalid, display the corresponding output statement using alert()
   if (num>0){
       if (checkUglyNumber(num)){
           alert(num+" is an ugly number");
           return;
       }
       else{
           alert(num+" is not an ugly number");
           return;
       }
       
   }
}

function checkUglyNumber(num){
    // Check whether the num value is an ugly number or not. If yes, return true. Else, return false
    if (num>0){
        var factors=[2,3,5];
        for (var i=0; i<factors.length; i++){
            while(num%factors[i]===0){
                num/=factors[i];
            }
        }
        return num==1;
    }
    else {
        return false;
    }    
}
