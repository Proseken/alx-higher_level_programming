#!/usr/bin/node

const callMeMoby = function (x, theFunction) {
  for (let index = 0; index < x; index++) {
    theFunction();
  }
};
module.exports = {
  callMeMoby
};
