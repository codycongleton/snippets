from os import lseek
import requests
import json
#get weather
response = requests.get("https://api.openweathermap.org/data/3.0/onecall?exclude=minutely,hourly,alerts&units=imperial&lat=44.058174&lon=-121.315308&exclude=minutely&appid=556590e0fedee56985f25b0bcc6a1208")
#open (create) file
f = open("weathertest.txt", "w")
#write contents of api response
f.write(str(response))
f.close()

# takes str "response" and formats it into json
ftext = json.dumps(response.json(), indent=4, separators=(". ", " = "))
print(ftext)
