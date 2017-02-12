var daysUntilMyBirthday = 3;
if (daysUntilMyBirthday > 30)
  output = daysUntilMyBirthday + " days until my birthday. Such a long time... :(";
else if (daysUntilMyBirthday == 0)
  output = "♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•* \n" +
  "♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪ \n" +
  "*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•« " ;
else
  output = daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY !!!"
console.log(output);
