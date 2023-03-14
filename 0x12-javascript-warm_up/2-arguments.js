#!/usr/bin/node
const args = process.argv.slice(2);
const num = args.length;

if (num === 0) {
  console.log('No argument');
} else if (num === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
