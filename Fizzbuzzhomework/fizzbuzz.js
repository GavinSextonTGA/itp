
for (let i = 1; i <= 100; i++) {
    if(i % 5 === 0 && i % 3 === 0){
        console.log ("fizzbuzz");
    }else if(i % 3 === 0 ) {
    console.log ("fizz");
        } else if(i % 5 === 0){
    console.log ("buzz");
    //
         } else {
        console.log(i);
    }
}

let midiNote = 64;
if (midiNote < 64) {
  console.log("MIDI note is smaller than 64.");
} else if (midiNote > 64) {
  console.log("MIDI note is greater than 64.");
} else {
  console.log("MIDI note is equal to 64.");
}