#!/usr/bin/node
const args = process.argv.slice(2);

if (Number.isInteger(parseInt(args[0]))) {
  for (let index = 0; index < args[0]; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
