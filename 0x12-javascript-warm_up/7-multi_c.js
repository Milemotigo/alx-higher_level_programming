#!/usr/bin/node

// prints x times “C is fun”
const args = process.argv.slice(2);
const count = parseInt(args);
if (!count) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < args; i++) {
  console.log('C is fun');
}
