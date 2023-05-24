#!/usr/bin/node

const fs = require('fs');
// const content = "Python is cool!"

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err) {
    if(err){
        console.error(err);
        return;
    }
    
});
