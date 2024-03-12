class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || Number.isInteger(w) === false || Number.isInteger(h) === false) {
      return 'Rectangle {}';
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const char = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
