#!/usr/bin/node

// prints My number: <first argument converted to an integer>
const indexLabel = 'My number';
const arg = process.argv[2];
const convertedArg = parseInt(arg);

if (isNaN(convertedArg)) {
  console.log('Not a number');
} else {
  console.log(`${indexLabel}: ${convertedArg}`);
}
