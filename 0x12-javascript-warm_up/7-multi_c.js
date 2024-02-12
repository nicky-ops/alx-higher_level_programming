#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('Missing number of occurrences');
} else if (parseInt(process.argv[2]) <= 0) {
  } else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
