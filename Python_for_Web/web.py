# working with web apis
# What is api?
# Api is a set of routines,protocols,and prebuilding tools for
# building software applications.
# an API specifies how software components should interact


# what is an web api?
# Web api is a framework for building HTTP services that can be consumed
# by a broad range of clients including browsers,moiles,iphone,tabltes.


# request library for sending request to apis
# pip install requests
import requests

fb_id = 4

url = "http://graph.facebook.com/{}/picture?type=large".format(fb_id)
r = requests.get(url)
print(type(r))
print(r.url)

print(r.content)

with open("profile.jpg", "wb") as file:
    file.write(r.content)


# google map api
mapurl = "http://maps.googleapis.com/maps/api/geocode/json"
parameters = {
    "address": "coding blocks pitampura"
}

res = requests.get(url=mapurl, params=parameters)
print(res.url)
content = res.content.decode('UTF-8')
print(content)


# POST requests
# use pastebin api,login and take your key

key = "124535"
postUrl = "https://pastebin.com/api/api_post.php"
data = {
    "api_dev_key": key,
    "api_option": "paste",
    "api_paste_code": "Hello how are you"
}

response = requests.post(url, data=data)
print(response.content)


# Web scraping
# Beautiful Soup
# This is a python library for pulling data out of html and xml files.
# pip install bs4
# pip install html5lib
""" 

WARNING: You are using pip version 20.1; however, version 21.2.4 is available.
You should consider upgrading via the 'c:\users\saswat\appdata\local\programs\python\python38\python.exe -m pip install --upgrade pip' command.
 """
