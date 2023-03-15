#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    while (number >= 0) {
      const remainder = number % base;
      number = Math.floor(number / base);
      if (remainder < 10) {
        return remainder.toString() + '';
      } else {
        return (String.fromCharCode(remainder + 87) + '') || '0';
      }
    }
  };
};
