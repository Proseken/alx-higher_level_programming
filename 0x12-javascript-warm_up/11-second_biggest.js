#!/usr/bin/node
const args = process.argv.slice(2);
let num = 0;
let prev = 0;

if (args.length <= 1) {
  console.log(0);
} else {
  args.forEach(el => {
    if (parseInt(el) > num) {
      prev = num;
      num = parseInt(el);
    }
  });
  console.log(prev);
}
