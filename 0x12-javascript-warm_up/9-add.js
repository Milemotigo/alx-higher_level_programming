#!/usr/bin/node

// prints the addition of 2 integers
const args = process.argv.slice(2);
const nums = parseInt(args);
if (!nums || args.length <= 1) {
    console.log('NaN');
}
else if (args > 1) {
    let add = parseInt(args[0]) + parseInt(args[1]);
    console.log(add);
}