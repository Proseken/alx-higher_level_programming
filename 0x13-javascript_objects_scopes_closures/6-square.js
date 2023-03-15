#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c = 'X') {
    let chaar = 'X';
    if (c !== 'X') {
      chaar = c;
    }
    for (let index = 0; index < this.height; index++) {
      let x = '';
      for (let ind = 0; ind < this.width; ind++) {
        x += chaar;
      }
      console.log(x);
    }
  }
}

module.exports = Square;
