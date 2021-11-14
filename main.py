import discord
import os
import requests
import random
import wolframalpha
from urllib.request import urlretrieve
from random import randint 


app_id = os.environ['wolframa']
nasa = os.environ['nasa']

client = discord.Client()
wolf = wolframalpha.Client(app_id)


def fetchAPOD(date):
  URL_APOD = "https://api.nasa.gov/planetary/apod?api_key="+nasa
  date = date
  params = {
      'date':date,
      'hd':'True'
  }
  response = requests.get(URL_APOD,params=params).json()
  return response['hdurl'] 


def mars():
  
  for i in range(850):
	  num = randint(0, 850)

  url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key="+nasa
  
  response = requests.get(url).json()
 
  response = response["photos"][num]
  return response["img_src"]


def ask(query):
  question = query
  res = wolf.query(question)
  answer = next(res.results).text
  return answer


def nasaEarth(lon, lat):
  url = "https://api.nasa.gov/planetary/earth/assets?lon="+lon+"&lat="+lat+"&date=2021-03-11&api_key="+nasa

  response = requests.get(url).json()
  
  return response['url']

def closeAsteroid(startDate, endDate):
  url = "https://ssd-api.jpl.nasa.gov/cad.api"

  params = {'date-min':startDate, 'date-max':endDate, 'sort':'dist', 'fullname':'true'}
  
  response = requests.get(url, params=params).json()
  return response['data'][0]

def coolPic(name):
  url = "https://images-api.nasa.gov/search?q=" + name + "&media_type=image"

  response = requests.get(url).json()
  num = min(100,len(response['collection']['items']))

  rand = randint(0,num-1)

  return response['collection']['items'][rand]['links'][0]['href']

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
  

@client.event

async def on_message(message):
  if message.author == client.user:
    return

  elif message.content.startswith('$pce '):
    if len(message.content) > 5:
      text = message.content[5:]
      await message.channel.send(fetchAPOD(text))

  elif message.content.startswith('$tlt '):
    if len(message.content) > 5:
      lon, lat = message.content[5:].split()
      await message.channel.send(nasaEarth(lon,lat))

  elif message.content.startswith('mar$'):
    if len(message.content) == 4:
      await message.channel.send(mars())

  elif message.content.startswith('a$k '):
    if len(message.content) > 4:
      query = message.content[4:]
      await message.channel.send(ask(query))
  
  elif message.content.startswith('a$t '):
    if len(message.content) > 4:
      startDate, endDate = message.content[4:].split(' ')
      asteroid = closeAsteroid(startDate, endDate)
      
      bot_message = "The closest asteroid passing by earth in this time range is " + asteroid[-1] + " at a distance of " + asteroid[4] + " AU, or " + str(int(float(asteroid[4])*9.296*10**7)) + " miles"
      
      await message.channel.send(bot_message)
  
  elif message.content.startswith('$Give me a picture of '):
    if len(message.content) > 22:
      search = message.content[22:]
      pic = coolPic(search)
      
      await message.channel.send(pic)

  elif message.content.startswith('$help'):
    help = "*```$pce YYYY-MM-DD```* to return NASA's space picture of the day for that date\n\n*```$tlt Longtitude Latitude```* to return a satellite image at that coordinate\n\n*```mar$```* to return a random picture taken by the Mars rover\n\n*```a$k {query}```* to return the answer to a space-related query\n\n*```a$t YYYY-MM-DD YYYY-MM-DD```* to return the name and distance of the closest asteroid passing by Earth in this time range\n\n*```$Give me a picture of {query}```* to return a random space-related picture of the query"
    await message.channel.send(help)
      
  

client.run(os.getenv('key'))


