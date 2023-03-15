#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  list.forEach(ele => {
    if (searchElement === ele) {
      nb++;
    }
  });
  return nb;
};
