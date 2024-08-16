#!/usr/bin/node

const { argv } = require('node:process');
const args = argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = [...new Set(args)].sort((a, b) => b - a);

  if (sortedArgs.length < 2) {
    console.log(0);
  } else {
    console.log(sortedArgs[1]);
  }
}
