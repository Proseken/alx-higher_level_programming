#!/usr/bin/node
const args = process.argv.slice(2);

if (Number.isInteger(parseInt(args[0]))) {
  console.log('My number: ' + Math.floor(args[0]));
} else {
  console.log('Not a number');
}
