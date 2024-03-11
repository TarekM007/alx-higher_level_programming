#!/usr/bin/node
const argument = process.argv[2];
const intVal = parseInt(argument);
if (Number.isInteger(intVal)) {
  for (let i = 0; i < intVal; i++) {
    let row = '';
    for (let j = 0; j < intVal; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
