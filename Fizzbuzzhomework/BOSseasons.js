let monthnumb = parseInt(prompt("Input a number 1 - 12"));
if (monthnumb >= 4 && monthnumb <= 6) {
    console.log("It is spring!");
} else if (monthnumb >= 7 && monthnumb <= 9) {
        console.log("It is summer");
}else if (monthnumb >= 10 && monthnumb <= 11) {
    console.log("It is fall ");
}else if (monthnumb === 12 || monthnumb >= 1 && monthnumb <= 3) {
    console.log("It is winter :(");
}else console.log("not a valid number")``