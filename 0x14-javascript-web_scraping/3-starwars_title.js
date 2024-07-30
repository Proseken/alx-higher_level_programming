#!/usr/bin/node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');
const movieId = process.argv[2];

request.get('https://swapi-api.alx-tools.com/api/films/'.concat(movieId),
  (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const movie = JSON.parse(body).title;
    console.log(movie);
  });
