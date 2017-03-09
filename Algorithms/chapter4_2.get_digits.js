// Create a JavaScript function that given a string, returns the integer made from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1,357,924,680
function getDays(str){
  var num = [];
  var res="";
  // console.log ( typeof str.charAt(1)); //This will always be string so cant use
for (var i=0;i<str.length;i++)
    if (str[i] >=  0) //This will convert str[i] to number , since its a number and ur 0 doesnt have quotes
      res+= str[i];
console.log(Number(res));
}

getDays("0s1a3y5w7h9a2t4?6!8?0");
