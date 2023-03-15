#!/usr/bin/node

class Rectangle {
  // an empty class Rectangle that defines a rectangle:
  constructor (w, h) {
    if (w && h) {
      if (!(h <= 0 || w <= 0)) {
        this.width = w;
        this.height = h;
      }
    }
  }
}

module.exports = Rectangle;
