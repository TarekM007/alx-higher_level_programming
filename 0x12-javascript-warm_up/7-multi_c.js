#!/usr/bin/node
const argument = process.argv[2];
const intVal = parseInt(argument);
if (Number.isInteger(intVal)) {
  for (let i = 0; i < intVal; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
