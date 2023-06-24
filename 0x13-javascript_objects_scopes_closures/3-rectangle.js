#!/usr/bin/node

// class rectangle
class Rectangle {
  constructor (w, h) {
    if (h >= 0 || w >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const char = 'X';
    for (let col = 0; col < this.height; col++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
