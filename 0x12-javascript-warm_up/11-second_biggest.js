#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 2) {
  console.log(0);
} else {
  let secondBiggest = 0;
  let biggest = 0;

  for (let index = 2; index < argv.length; index++) {
    if (parseInt(argv[index]) > biggest) {
      secondBiggest = biggest;
      biggest = parseInt(argv[index]);
    }
  }

  console.log(secondBiggest);
}
