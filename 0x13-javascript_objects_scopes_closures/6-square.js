#!/usr/bin/node
const SquareX = require('./5-square');

class Square extends SquareX {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let rec = c.repeat(this.width);
      console.log(rec);
    }
  }
}
module.exports = Square;
