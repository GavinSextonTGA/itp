let i = parseInt(prompt("Input a number"))  // pre remembering for loops
function func(count) {
    if (count < 0) {
      return;
    }
    
    if (count%2 == 0) console.log(`# # # # `);
    if (count%2 == 1) console.log(` # # # `);

    func(count - 1);
  }
  func(i - 1);


  //oh right for loops
  let size = parseInt(prompt("Input a number"))
  for (let i = 1; i <= size; i++)
    if(i%size ==0 )
        console.log (i);
    else console.log ("idk man");
  
    //i can't anymore just take the first one i guess
     
      
   
    