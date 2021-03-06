# AstrnOt-Bot
This project utilizes several of NASA's API's to create a discord bot using Python. The bot responds to a number of commands to return space-related facts and pictures.

<img src="https://user-images.githubusercontent.com/67729867/141670244-e4b203e7-137f-4554-8fb8-268cc7f68415.jpg" width="200" height="200" />

## What it does
The discord bot recognizes a total of 7 commands that it will respond to in the form of a discord message. The commands are also in the form of discord messages:
- **$help** returns a list of recognized commands and their functionality
- **$pce YYYY-MM-DD** returns NASA's space picture of the day for a given date
- **$tlt Longitude Latitude** returns a satellite image of the given longitude and latitude coordinates
- **mar$** returns a random picture of the Martian landscape taken by the Mars rovers
- **a$k {query}** returns the answer to a space-related query
- **a$t YYYY-MM-DD YYYY-MM-DD** returns the name and pass-by distance of the closest asteroid passing by Earth within the given time range
- **$Give me a picture of {query}** returns a random picture related to the query from NASA's image database
