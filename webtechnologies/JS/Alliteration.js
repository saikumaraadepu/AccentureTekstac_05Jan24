//Dont change or delete the try/catch block
function checkAlliteration(){
    try{
        // Get the value of char & alliter components
        var char= document.getElementById("char").value.toLowerCase();
        var sentence= document.getElementById("alliter").value.toLowerCase();
        
        // Invoke getCount() method - will return the number of words.
        var wordCount = getCount(sentence);
        
        // IF the number of words in the sentence is <3, display the corresponding output statement in div with id 'result' 
        if (wordCount < 3) {
            document.getElementById("result").innerHTML = "Invalid number of words";
        }
        // ELSE, invoke validateSentence() method - will return true / false. 
        else {
            // IF false, display the corresponding output statement in div with id 'result'
            if (!validateSentence(sentence)) {
                document.getElementById("result").innerHTML = "Invalid sentence";
            } 
            else {
                // ELSE, Invoke getScore() - will return the calculated score.
                var score = getScore(sentence, char);
                
                // Display the corresponding output statement in div with id 'result'
                document.getElementById("result").innerHTML = "Your score is " + score;
            }
        }
    return false;
    } catch(err) {
        document.getElementById("result").innerHTML = "Function checkAlliteration: " + err;
    }
}

function getCount(str){
    try{
        // Calculates the number of words in str returns the count
        var words = str.split(" ");
        return words.length;
    } catch(err) {
        document.getElementById("result").innerHTML = "Function getCount: " + err;
    }
}

function validateSentence(str){
    try {
        // When any word of str starts with a vowel, return false; else, return true
        var words = str.split(" ");
        for (var i = 0; i < words.length; i++) {
            if ("aeiouAEIOU".includes(words[i][0])) {
                return false;
            }
        }
        return true;
    } catch(err) {
        document.getElementById("result").innerHTML = "Function validateSentence: " + err;
    }
}

function getScore(str,char){
    try{
    // Compare the first letter of every word from str with char, calculate and return the score
    var score=0;
    var words=str.split(" ");
    if(words[0].charAt(0)!==char){
        score=0;
        return score;
    }
    
    for (var i=1; i<words.length; i++){
        if (i<3 && words[i].charAt(0)===char){
            score+=1;
        }
        else if (i>=3 && words[i].charAt(0)===char){
            score+=2;
        }
        else {
            break;
        }
    }
    return score;
    }catch(err){
        document.getElementById("result").innerHTML="Function getScore: "+err;
    }
}
