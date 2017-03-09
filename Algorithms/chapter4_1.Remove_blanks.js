// Create a function that, given a string, returns the string, without blanks. Given " play that Funky Music ", returns a string containing "playthatFunkyMusic"

function removeSpaces (str)
{
  var res = "";
var hi = null; //Yup just doing somehtinf
  for (var i=0; i<str.length;i++)
  {
    // if (str.charAt(i) == " ")
    if (str[i] == " ")
       continue;
    res += str.charAt(i);
  }
  return res;


}

console.log(removeSpaces("Play That Funky Music"));
