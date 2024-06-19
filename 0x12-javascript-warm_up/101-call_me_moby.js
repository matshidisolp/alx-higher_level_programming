#!/usr/bin/node
/* executes x times a function- visible from outside */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
