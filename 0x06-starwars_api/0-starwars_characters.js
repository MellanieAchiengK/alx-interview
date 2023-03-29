#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    process.exit(1);
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  for (let characterUrl of characters) {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(`Error: ${error}`);
        process.exit(1);
      }

      if (response.statusCode !== 200) {
        console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
        process.exit(1);
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
