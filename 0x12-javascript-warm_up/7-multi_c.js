#!/usr/bin/node

// prints x times “C is fun”
const args = process.argv.slice(2);
const count = parseInt(args[0]);
for (let i = 0; i < count; i++) {
  console.log('c is fun');
}
