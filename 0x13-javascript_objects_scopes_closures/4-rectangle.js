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

  print () {
    for (let index = 0; index < this.height; index++) {
      let x = '';
      for (let ind = 0; ind < this.width; ind++) {
        x += 'X';
      }
      console.log(x);
    }
  }

  rotate () {
    const a = this.width;
    this.width = this.height;
    this.height = a;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
