#!/usr/bin/node

let nd = 0;
exports.logMe = function (item) {
  console.log(nd + ': ' + item);
  nd++;
};
