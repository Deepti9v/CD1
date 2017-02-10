// If You Don't Mind, Can I Have The Time?
// Create a program that will tell you the time.
// With the following variables...
// var HOUR = 8;
// var MINUTE = 50;
// var PERIOD = "AM";
// Copy
// ...your program should print "It's almost 9 in the morning"
// And when changed to...
// var HOUR = 7;
// var MINUTE = 15;
// var PERIOD = "PM";
// Copy
// ...your program should print "It's just after 7 in the evening"
// Challenge:
// If minutes less than 30, "just after" the hour, more than 30, "almost" the next hour
// AM / PM, "in the morning", "in the evening",
// HINT
// You can add as many items into console.log as you need (They will be separated with spaces)

var HOUR = 8;
var MINUTE = 30;
var PERIOD = "AM";
var output = "";

if (MINUTE > 30)
  output = "It's almost " + (HOUR+1);
else if (MINUTE < 30)
  output  = "It's just after " + (HOUR);
else
  output ="It's exactly " + HOUR + ":" + 30; //This is the border case

if (PERIOD == "AM")
  output += " in the morning";
else if (PERIOD == "PM")
  output += " in the evening";

console.log(output);
