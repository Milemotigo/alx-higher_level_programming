#!/usr/bin/node

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

const fs = require('fs');

fs.writeFile(filePath, contentToWrite, 'utf-8', (error) => {
  if (error) {
    error.log(error);
  }
});
