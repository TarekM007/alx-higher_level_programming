#!/usr/bin/node
function fact (a) {
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
const arg = process.argv[2];
if (arg === undefined) {
  console.log('1');
}
const intVal = parseInt(arg);
const result = fact(intVal);
console.log(result);
