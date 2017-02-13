// You Say It’s Your Birthday
// If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day....",
//
// Example: given yourBirthday(4,19) or yourBirthday(19,4)

function yourBirthday(first,second)
{
  if ((first >=1 && first <= 31) && (second >=1 && second <= 12))
    console.log("How did you know?");
  else if  ((second >=1 && second <= 31) && (first >=1 && first <= 12))
    console.log("How did you know?");
  else
    console.log("Just Another day ...");
}

yourBirthday(31,1);
yourBirthday(32,1);
yourBirthday(1,20);
