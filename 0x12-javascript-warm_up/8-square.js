#!/usr/bin/node
const x = process.argv[2];
if (!parseInt(x)) {
  console.log('Missing size');
} else {
  let myVar = '';
  for (let j = 0; j < parseInt(x); j++) {
    myVar = myVar + 'X'.repeat(parseInt(x)) + '\n';
  }
  console.log(myVar);
}
