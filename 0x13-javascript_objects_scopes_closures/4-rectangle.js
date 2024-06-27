#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (arguments.length !== 2 || w <= 0 || w === undefined || h <= 0 || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '';

      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
