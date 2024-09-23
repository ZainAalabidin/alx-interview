#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

// Check if a movie ID is passed as an argument
if (!movieId) {
    console.error("Usage: ./0-starwars_characters.js <movie_id>");
    process.exit(1);
}

// Base URL for the Star Wars API films endpoint
const url = `https://swapi.dev/api/films/${movieId}/`;

// Function to get and print character names
request(url, (error, response, body) => {
    if (error) {
        console.error("Error:", error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error("Failed to fetch data. Status code:", response.statusCode);
        return;
    }

    // Parse the response body as JSON
    const data = JSON.parse(body);
    const characters = data.characters;

    // Fetch and print each character's name
    characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
                console.error("Error:", charError);
                return;
            }

            if (charResponse.statusCode === 200) {
                const characterData = JSON.parse(charBody);
                console.log(characterData.name);
            }
        });
    });
});

