import logging
import json
import requests
#import mysql.connector

def getCounties():
    url = "https://api.covidactnow.org/v2/counties.json?apiKey=ac57d3d71f0b4cd098c095fc77867f3e"
    response = requests.get(url)
    checkHttp(response)
    fileResponse = response.json()
    return fileResponse

def checkHttp(response):
    if response.status_code != 200:
        logging.critical("API authorization HTTP status code: ", response.status_code)
        raise Exception("Authorization failed, check credentials, verify access, and try again")

def printInfoPretty(info_dict):
    print(json.dumps(info_dict, indent=4, sort_keys=False))

def getMD():
    listOfData = getCounties()
    for i in listOfData:
        if i['state'] == 'MD':
            print(i)



if __name__ == "__main__":
    getMD()
