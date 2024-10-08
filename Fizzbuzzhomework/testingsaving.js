// if
let midiNote = 64;
if (midiNote < 0 || midiNote > 127) {
  console.log("The note value entered is an invalid MIDI note.");
}
if (midiNote >= 0 && midiNote <= 127) {
  console.log("The note value entered is a valid MIDI note.");
  console.log("MIDI note value is", midiNote);
}
// if-else
let midiNote = 64;
if (midiNote <= 0 || midiNote >= 127) {
  console.log("The note value entered is Invalid.");
} else {
  console.log("The note value entered is valid.");
}
// else-if
let midiNote = 64;
if (midiNote < 64) {
  console.log("MIDI note is smaller than 64.");
} else if (midiNote > 64) {
  console.log("MIDI note is greater than 64.");
} else {
  console.log("MIDI note is equal to 64.");
}
// nested if-else
let midiNote = parseInt(prompt("What's your favorite midiNote? "));
if (midiNote < 64) {
  console.log("MIDI note is smaller than 64.");
  if (midiNote === 48) {
    console.log(`The note name for ${midiNote} is C2.`);
  } else if (midiNote === 40) {
    console.log(`The note name for ${midiNote} is E1.`);
  }
} else {
  console.log("MIDI note is greater than or equal to 64.");
}