#!/usr/bin/node
console.log(parseInt(process.argv[2]) ? 'C is fun\n'.repeat(parseInt(process.argv[2]) - 1) + 'C is fun' : 'Missing number of occurences');
