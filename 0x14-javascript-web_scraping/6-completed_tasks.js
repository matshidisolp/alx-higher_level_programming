#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const tasks = JSON.parse(body);
      const completedTasks = {};

      tasks.forEach(task => {
        if (task.completed) {
          if (!completedTasks[task.userId]) {
            completedTasks[task.userId] = 0;
          }
          completedTasks[task.userId] += 1;
        }
      });

      console.log(completedTasks);
    } catch (err) {
      console.error('Error parsing JSON:', err);
    }
  }
});
