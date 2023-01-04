var birthYear = prompt("What year were you born?");

if (1997 >= birthYear && birthYear >= 2012) {
    console.log("Gen Z");}
else if (birthYear >= 1981 && birthYear <= 1996) {
    console.log("Millenial");}
else if (birthYear >= 1965 && birthYear <= 1980) {
    console.log("Gen X");}
else if (birthYear >= 1946 && birthYear <= 1964) {
    console.log("Boomer");}