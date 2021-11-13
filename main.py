import discord
import os
import requests
from urllib.request import urlretrieve



client = discord.Client()


def fetchAPOD(date):
  URL_APOD = "https://api.nasa.gov/planetary/apod?api_key=4Fe8SgIiEu2tP2N5OoKI8nolBbzrpuMMcwKmZkDl"
  date = date
  params = {
      'date':date,
      'hd':'True'
  }
  response = requests.get(URL_APOD,params=params).json()
  return response['hdurl'] 


def nasaEarth(lon, lat):
  url = "https://api.nasa.gov/planetary/earth/imagery?lon="+lon+"&lat="+lat+"&date=2015-03-11&api_key=4Fe8SgIiEu2tP2N5OoKI8nolBbzrpuMMcwKmZkDl"

  return url



@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  
 

@client.event

async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$pce '):
    if len(message.content) > 5:
      text = message.content[5:]
      await message.channel.send(fetchAPOD(text))

  if message.content.startswith('$tlt '):
    if len(message.content) > 5:
      lon, lat = message.content[5:].split()
      await message.channel.send(nasaEarth(lon,lat))

client.run(os.getenv('key'))

'''
def get_image(lat, lon):
  token = "mfers wont let me get a token by signing up"
  zoom = 16
  url = ("https://catalog-api.hibirdi.com/catalog/lat/{}/lng/{}/zoom/{}/token/"
       .format(lat, lon, zoom, token))
  return url 
'''


