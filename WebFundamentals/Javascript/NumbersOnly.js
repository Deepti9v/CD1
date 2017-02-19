// var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);
// // newArray is [1, -3, 0.5]
var numbersOnly = function(arr){
  output = [];
  for (var i=0;i<arr.length;i++)
   { if (typeof arr[i] === "number")
      output.push(arr[i]);
   }
   console.log(output);
   return output;
}
numbersOnly([1, "apple", -3, "orange", 0.5]);
