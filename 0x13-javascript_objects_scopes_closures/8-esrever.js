#!/usr/bin/node

exports.esrever = function (list) {
    const revcount = [];
  
    for (let i = list.length - 1; i >= 0; i--) {
      revcount.push(list[i]);
    }
  
    return revcount;
  };