#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  const args = process.map(Number).slice(2, len).sort((a, b) => a - b);

  console.log(args[len - 2]);
}
