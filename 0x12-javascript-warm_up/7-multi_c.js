#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2]) {
  const x = parseInt(argv[2]);
  if (x) {
    for (let index = 0; index < x; index++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
}
