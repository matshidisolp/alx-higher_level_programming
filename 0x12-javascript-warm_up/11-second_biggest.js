#!/usr/bin/node
/* prints the 2nd largest integer from a list of arguments */
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const sortedArgs = process.argv.slice(2).map(Number).sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
