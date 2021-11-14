from os import path, remove
import pathlib
import requests
import json

response = requests.get("https://my-json-server.typicode.com/paul5511/jsonparser/sites")
resp = response.text

jsonBlob = json.loads(resp)

fileName = "output.csv"
if(path.exists(fileName)):
    remove(fileName)

f = open(fileName, "x")


f.write("ID,SiteName" + "\n")

for x in jsonBlob:
    lineToWrite = str(x["id"]) + "," +x["siteName"]
    print(lineToWrite)
    f.write(lineToWrite + "\n")

f.close()



