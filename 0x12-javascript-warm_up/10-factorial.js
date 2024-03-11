#!/usr/bin/node
function fact (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a === 0) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
const arg = process.argv[2];
const intVal = parseInt(arg);
const result = fact(intVal);
console.log(result);
