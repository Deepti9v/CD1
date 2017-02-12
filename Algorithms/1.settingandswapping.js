// Setting and Swapping
// Set variable myNumber to 42. Set variable myName to your name. Now swap myNumber into myName & vice versa.
var myNumber = 42;
var myName = "Deepti";
var tmp;

tmp = myNumber;
myNumber = myName;
myName = tmp;

console.log("myNumber value "+myNumber);
console.log("myName value "+myName);
