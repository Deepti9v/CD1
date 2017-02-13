// Write a function that determines whether a given year is a leap year. If a year is divisible by four, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.
function leapYear(year)
{
  if (year%4 == 0 && year%100!=0)
    console.log("Leap year");
  else if (year%400 == 0)
    console.log("Leap year");
  else
    console.log("Not a leap year");
}

leapYear(1904);
leapYear(2016);
leapYear(2000);

/*
Precedence order
(),[],
++,--,!,
/,*,%
+,-,
>,>=, <, <=
==, !=, ===, !==
&&
||
?:
=
*/
