#!/usr/bin/node

// prints the addition of 2 integers
const args = process.argv.slice(2);
const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);
if (args.length <= 1) {
    console.log('NaN');
}
else if (!num1 || !num2) {
    console.log('NaN');
}
else {
    let add = num1 + num2;
    console.log(add);
}