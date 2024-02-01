//Don't change or delete the try/catch block
function signIn(){
    try{
       //Get the values of elements using DOM
       var name=document.getElementById("name").value;
       var password=document.getElementById("password").value;
       var output=document.getElementById("demo");
       
       //Invoke the passwordValidate() method
       //Display the result as per the requirement in the description
       if (passwordValidate(password))
       {
           output.innerHTML="Sign In successful!!! Welcome "+name+" Learn More with BigStorm";
       }
       else 
       {
         output.innerHTML="Please enter a valid password (password should be of minimum 8 characters having at least 1 small letter(a-z),1 capital letter(A-Z), 1 digit(0-9), 1 special character)";
       }
    }catch(err){
        document.getElementById("demo").innerHTML="Function signIn: "+err;
    }
    return false;
}

function passwordValidate(password){
  try{
    //Validate the password (password should be of minimum 8 characters - having atleast 1 small letter(a-z),1 capital letter(A-Z), 1 digit(0-9), 1 special character)
    //return true or false based on validation
    var regex=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;
    return regex.test(password);
    }catch(err){
        document.getElementById("demo").innerHTML="Function passwordValidate: "+err;
    }
}
