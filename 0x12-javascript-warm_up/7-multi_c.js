#!/usr/bin/node

// prints x times “C is fun”
const args = process.argv.slice(2);
for (let i = 0; i < args; i++) {
  console.log('c is fun');
}
