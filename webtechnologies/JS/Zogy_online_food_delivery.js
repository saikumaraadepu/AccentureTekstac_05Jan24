function show_value(x){
    document.getElementById("demo").innerHTML=x;
}
function displayFeedbackMessage()
{
 try {
       //Get the name and feedback range value using DOM functions
       var name=document.getElementById("cname").value;
       var range=document.getElementById("rate").value;
       var message="";
       if (range>=1 && range<=10)
       {
           if (range>=1 && range<=5)
           {
               message="Hi "+name+" Thank you for your valuable feedback. Sorry for the inconvenience. You will be contacted by our customer care officer soon";
           } 
           else if (range>5 && range<=8)
           {
               message="Hi "+name+" Thank you for your valuable feedback. You can post your complaints on customercare@gmail.com";
           } 
           else if (range>8)
           {
               message="Hi "+name+" Thank you for your valuable feedback. Happy customers are our only asset";
           }
       }
       
       //Display the output based on feedback range in div with id "result"
       document.getElementById("result").innerHTML=message;
   } catch(err) {
       document.getElementById("result").innerHTML=err;
   }return false;
}