#!/usr/bin/node
console.log(parseInt(process.argv[2]) ? 'C is fun\n'.repeat(parseInt(process.argv[2])) : 'Missing number of occurences');
