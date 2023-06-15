#!/usr/bin/node

// class rectangle
class Rectangle {
    constructor (w, h) {
        if (h >= 0 || w >= 0) {
            this.width = w;
            this.height = h;
        }
    }
    print() {
        let char = 'X';
        for (let col = 0; col < this.height; col++) {
            console.log(char.repeat(this.width));
        }
    }
    double() {
        this.width *= 2;
        this.height *= 2;
    }
    rotate() {
        const rot = this.width;
        this.width = this.height;
        this.height = rot;
    }
}
module.exports = Rectangle;