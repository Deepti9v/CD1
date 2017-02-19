var slot_machine =  function(quarters){
  var number = Math.ceil(Math.random()*(100-50+1))+50 ;
    return (quarters + number);
}
console.log(slot_machine(2));
