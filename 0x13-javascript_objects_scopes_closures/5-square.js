#!/usr/bin/node
const Rectangle = require('./4-rectangle');

// child class
class Square extends Rectangle {
    constructor(size) {
        super(size)
        this.size = size;
    }
    square() {
        this.size *= this.size;
    }
};
module.exports = Square;