#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] && parseInt(argv[2])) {
  const size = parseInt(argv[2]);
  if (size) {
    for (let index = 0; index < size; index++) {
      console.log('X'.repeat(size));
    }
  }
} else {
  console.log('Missing size');
}
