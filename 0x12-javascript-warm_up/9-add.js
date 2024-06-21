#!/usr/bin/node

function add (a, b) {
  const result = Number(a) + Number(b);
  return result;
}

const [firstArg, secArg] = process.argv.splice(2);
console.log(add(firstArg, secArg));
