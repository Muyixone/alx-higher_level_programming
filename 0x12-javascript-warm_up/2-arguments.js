#!/usr/bin/node

function printArg () {
  if (process.argv.length === 3) {
    console.log('Argument found');
  } else if (process.argv.length <= 2) {
    console.log('No argument');
  } else {
    console.log('Arguments found');
  }
}

printArg();
