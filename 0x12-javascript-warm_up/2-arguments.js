#!/usr/bin/node
const argc = process.argv.length;

if (argc > 2) {
  if (argc > 3) {
    console.log('Arguments found');
  } else {
    console.log('Argument found');
  }
} else {
  console.log('No argument');
}
