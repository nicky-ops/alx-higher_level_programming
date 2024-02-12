#!/usr/bin/node
const x = process.argv[2];
if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < parseInt(x); j++) {
    let y = 0;
    let myVar = '';
    while (y < x) {
      myVar = myVar + 'X';
      y++;
    }
    console.log(myVar);
  }
}
