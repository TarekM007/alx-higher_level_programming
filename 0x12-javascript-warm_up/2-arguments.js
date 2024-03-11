#!/usr/bin/node
const argsCount = process.argv.length - 2;
if (argsCount >= 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
