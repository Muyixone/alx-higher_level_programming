#!/usr/bin/node

const [firstArg] = process.argv.splice(2);

if (firstArg !== undefined) {
  const result = firstArg * 1;

  if (isNaN(result)) {
    console.log('Not a number');
  } else {
    console.log(result);
  }
} else {
  console.log('Not a number');
}
