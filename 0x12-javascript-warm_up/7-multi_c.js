#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('Missing number of occurrences');
} else if (parseInt(process.argv[2]) <= 0) {
  } else {
  const message = 'C is fun\n';
  console.log(message.repeat(parseInt(process.argv[2]) - 1) + 'C is fun');
}
