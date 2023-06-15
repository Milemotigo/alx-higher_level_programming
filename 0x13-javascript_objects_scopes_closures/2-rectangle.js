#!/usr/bin/node

// class Rectangle
class Rectangle {
	constructor (w, h) {
		if (h === 0 || w === 0 || h <= 0 || w <= 0)
		{
			return;
		}
		this.width = w;
		this.height = h;
	}
}
module.exports = Rectangle;
