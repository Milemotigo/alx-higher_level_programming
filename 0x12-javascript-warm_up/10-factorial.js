#!/usr/bin/node

//  prints a factoriale
const args = process.argv.slice(2);
const num = parseInt(args);
function recursiveFunction(num) {
    if (num <= 0) {
        return (1);
    }
    return (num * recursiveFunction(num - 1));  
}
if (isNaN(num)) {
    console.log("1");
}
else {
    console.log(recursiveFunction(num));
}