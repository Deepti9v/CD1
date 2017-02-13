//print incoming
function what(incoming)
{
  console.log(incoming);
}
what("hi");
// Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?
var sum=0;
for (var i=-300000;i<=300000;i++)
{
  if (i%2 != 0)
    sum+=i;
}
console.log(sum);
// Countdown By Fours
// Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.
var i=2016;
while(i >= 0)
{
  console.log(i);
  i-=4;
}
// Flexible Countdown
// Based on earlier “Countdown By Fours”, given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR loop.
// Example: For (2,9,3), print 9 6 3 (on successive lines).
function flexCounter(lowNum,highNum,mult)
{
  for (var i= 9; i>= 2; i-=3)
  {  if (i%mult == 0)
        console.log(i);
  }
}
flexCounter(2,9,3);
