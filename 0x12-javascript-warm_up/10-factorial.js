#!/usr/bin/node

const { argv } = require('node:process');

function factorial (number) {
  number = parseInt(number);
  if (isNaN(number) || number === 0 || number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

console.log(factorial(argv[2]));
