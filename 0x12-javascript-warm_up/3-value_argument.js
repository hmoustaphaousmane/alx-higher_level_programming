#!/usr/bin/node

const { argv } = require('node:process');

if (argv.at(2)) {
  console.log(argv.at(2));
} else {
  console.log('No argument');
}
