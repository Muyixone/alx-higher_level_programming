#!/usr/bin/node

const [firstArg] = process.argv.splice(2);

if (firstArg !== undefined) {
  if (isNaN(firstArg) === false) {
    const res = Math.trunc(firstArg);
    console.log(`My number: ${res}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
