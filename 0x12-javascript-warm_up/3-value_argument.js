#!/usr/bin/node

// args
let argCount = process.argv;
if (argCount[2] === null) {
  console.log('No argument');
} else if (argCount[2]) {
  console.log(`${argCount[2]}`);
}
