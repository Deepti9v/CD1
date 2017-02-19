
var HashTable = function(size)
{
  this.data = [];
  this.capacity = size;
}

HashTable.prototype.get = function(key)
{
  var indx = hashing(key)%this.capacity;
  console.log(this.data[indx]);

}

HashTable.prototype.put = function(key,value)
{
  var indx = hashing(key)%this.capacity;


}

function hashing(word)
{
  var sum=0;
  for (var i=0;i<word.length;i++)
      sum+= word.charCodeAt(i);
  if (sum > 200)
      sum = sum%200;
  //console.log(sum);
    //console.log(word.charCodeAt(i));
}

var map = new HashTable(4);
hashing("hi");
map.put("location","la");
console.log(map.data);
console.log("getting the location");
map.get("location");

var a = [];
var b = [];
a[0] = b;
console.log(a.length);
console.log(a.isEmpty());
