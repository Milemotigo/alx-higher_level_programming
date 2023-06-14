#!/usr/bin/node

//prints a square
const args = process.argv.slice(2);
const count = parseInt(args);

if(!count) {
    console.log("Missing size");
}
for (let i = 0; i < count; i++) {
    let row = '';
    for (let a = 0; a < count; a++) {
      row += 'x';
    }
    console.log(row);
}