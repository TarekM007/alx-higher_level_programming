#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const intVal1 = parseInt(arg1);
const intVal2 = parseInt(arg2);
const result = add(intVal1, intVal2);
console.log(result);
