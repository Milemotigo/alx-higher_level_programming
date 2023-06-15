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
        let rectange = '';
        let right = '';
        for (let row = 0; row < this.height; row++)
        {
            for (let col = 0; col < this.width; col++)
            {
                rectange += 'X';
            }
            rectange += '';
        }
        console.log(rectange);
    }
}
module.exports = Rectangle;