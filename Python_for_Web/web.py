# working with web apis
# What is api?
# Api is a set of routines,protocols,and prebuilding tools for
# building software applications.
# an API specifies how software components should interact


# what is an web api?
# Web api is a framework for building HTTP services that can be consumed
# by a broad range of clients including browsers,moiles,iphone,tabltes.


#request library for sending request to apis
#pip install requests
import requests

fb_id = 4

url = "http://graph.facebook.com/{}/picture?type=large".format(fb_id)
r= requests.get(url)
print(type(r))
print(r.url)

print(r.content)

with open("profile.jpg", "wb") as file:
    file.write(r.content)


#google map api
mapurl = "http://maps.googleapis.com/maps/api/geocode/json" 
parameters = {
    "address": "coding blocks pitampura"
}   

res = requests.get(url=mapurl, params=parameters)
print(res.url)
content = res.content.decode('UTF-8')
print(content)