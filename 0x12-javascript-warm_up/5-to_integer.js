#!/usr/bin/node
const argument = process.argv[2];
if (argument === undefined) {
  console.log('Not a number');
} else {
  const intVal = parseInt(argument);
  if (Number.isInteger(intVal)) {
    console.log('My number: ' + intVal);
  } else {
    console.log('Not a number');
  }
}
