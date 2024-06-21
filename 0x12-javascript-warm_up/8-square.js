#!/usr/bin/node

const [myArg] = process.argv.splice(2);
let stringVal = '';

if (isNaN(myArg) === false) {
  for (let i = 0; i < myArg; i++) {
    for (let j = 0; j < myArg; j++) {
      stringVal += 'X';
    }
    stringVal += '\n';
  }
} else {
  console.log('Missing size');
}
console.log(stringVal);
