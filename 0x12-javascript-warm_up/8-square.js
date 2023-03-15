#!/usr/bin/node
const args = process.argv.slice(2);

if (Number.isInteger(parseInt(args[0]))) {
  for (let index = 0; index < args[0]; index++) {
    let x = '';
    for (let index = 0; index < args[0]; index++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
