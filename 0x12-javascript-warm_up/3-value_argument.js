#!/usr/bin/node

const [firstArg] = process.argv.splice(2);

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
