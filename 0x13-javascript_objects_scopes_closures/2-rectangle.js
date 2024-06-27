#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (arguments.length !== 2 || w <= 0 || w === undefined || h <= 0) {
      return;
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
