"""
   Author: Olaoluwa Idowu
   Title: Where is the space station?
   Date: 10-02-2022  
"""


# importing modules
import json
import urllib.request
import turtle
import time


# getting people's name and craft from api
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in space: ', result['number'])

people = result['people']

for p in people:
    print(p['name'], 'in', p['craft'] )



# getting iss position
url = 'http://api.open-notify.org/iss-now.json'   
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('latitude:', lat)
print('longitude: ', lon)



# setting screen to match coordinates
screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')

# changing turtle icon
screen.register_shape('iss2.gif')
iss = turtle.Turtle()
iss.shape('iss2.gif')
iss.setheading(90)


# going to iss current position
iss.penup()
iss.goto(lon,lat)


# plotting Houston's pass-over time
lat = 29.5502
lon = -95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()


url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
#print(result)
over = result['response'][1]['risetime']
#print(over)

style = ('Arial', 15, 'bold')
location.write(time.ctime(over),font=style)




# plotting Nigeria's pass-over time
lat = 6.521916948470381
lon = 3.37706844517766

location = turtle.Turtle()
location.penup()
location.color('white')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()


url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
#print(result)
over = result['response'][1]['risetime']
#print(over)

style = ('Arial', 15, 'bold')
location.write(time.ctime(over),font=style)


