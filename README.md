# AstrnOt-Bot

<img src="https://user-images.githubusercontent.com/67729867/141670244-e4b203e7-137f-4554-8fb8-268cc7f68415.jpg" width="200" height="200" />

## Overview

AstrnOt-Bot is a Python-based discord bot that utilizes several of NASA's API's to return space-related facts and pictures. The bot recognizes a total of 7 commands that it will respond to in the form of a discord message.
Functionality

The bot can respond to the following commands:

   - **$help** returns a list of recognized commands and their functionality
   - **$pce YYYY-MM-DD**  returns NASA's space picture of the day for a given date
   - **$tlt Longitude Latitude**  returns a satellite image of the given longitude and latitude coordinates
   - **mar$**  returns a random picture of the Martian landscape taken by the Mars rovers
   - **a$k {query}**  returns the answer to a space-related query
   - **a$t YYYY-MM-DD YYYY-MM-DD**  returns the name and pass-by distance of the closest asteroid passing by Earth within the given time range
   - **$Give me a picture of {query}**  returns a random picture related to the query from NASA's image database

## APIs Used

AstrnOt-Bot uses the following NASA APIs:

Astronomy Picture of the Day (APOD) API: to retrieve NASA's space picture of the day 
Earth Imagery API: to retrieve satellite images of specific longitude and latitude coordinates
Mars Rover Photos API: to retrieve random pictures of the Martian landscape taken by the Mars rovers
Near Earth Object Web Service API: to retrieve information on the closest asteroid passing by Earth within a given time range
Image and Video Library API: to retrieve random pictures related to the query from NASA's image database

## How to Use

To use the bot, simply enter one of the recognized commands in a discord message. The bot will then respond with the appropriate information or image.
Future Improvements

In the future, the bot could be improved by adding more space-related commands and features, such as information on specific planets or space missions. Additionally, the bot could be made more interactive by allowing users to ask follow-up questions or provide feedback on the information provided.
