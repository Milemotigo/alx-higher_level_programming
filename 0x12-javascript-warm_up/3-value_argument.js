#!/usr/bin/node

// args
function len (str) {
  let count = 0;
  let char = str[count];
  while (char !== undefined) {
    count++;
    char = str[count];
  }
  return count;
}

const args = process.argv.slice(2);
const argCount = len(args);

if (argCount === 0) {
  console.log('No argument');
} else if (argCount === 1) {
  console.log(`${args}`);
}
