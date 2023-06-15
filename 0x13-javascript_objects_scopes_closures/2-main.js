#!/usr/bin/node
const Rectangle1 = require('./2-rectangle');

const r1 = new Rectangle1(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle1(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle1(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle1(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);
