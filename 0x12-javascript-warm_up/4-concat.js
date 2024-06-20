#!/usr/bin/node

const [firstArg, secArg] = process.argv.splice(2);

if (firstArg === undefined) {
  console.log(`${firstArg} is ${secArg}`);
} else {
  console.log(`${firstArg} is ${secArg}`);
}
