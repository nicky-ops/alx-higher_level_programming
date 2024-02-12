#!/usr/bin/node
if (!parseInt(process.argv[2]) || parseInt(process.argv[2]) <= 0) {
  console.log('Missing number of occurrences');
} else {
  const message = 'C is fun\n';
  console.log(message.repeat(parseInt(process.argv[2])));
}
