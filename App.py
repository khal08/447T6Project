import logging
import json
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/vax_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#database configuration
class Data(db.Model):
    state = db.Column(db.String(80),primary_key = True)
    county = db.Column(db.String(100))
    vaccineRate = db.Column(db.String(100))


    def __init__(self,state, county, vaccineRate):
        self.state = state
        self.county = county
        self.vaccineRate = vaccineRate

#
def getCounties():
    url = "https://api.covidactnow.org/v2/counties.json?apiKey=ac57d3d71f0b4cd098c095fc77867f3e"
    response = requests.get(url)
    checkHttp(response)
    fileResponse = response.json()
    return fileResponse

# API error checking
def checkHttp(response):
    if response.status_code != 200:
        logging.critical("API authorization HTTP status code: ", response.status_code)
        raise Exception("Authorization failed, check credentials, verify access, and try again")

#run to view JSON data in viewable format
def printInfoPretty(info_dict):
    print(json.dumps(info_dict, indent=4, sort_keys=False))

@app.route('/')
def getStates():
    listOfData = getCounties()

    for i in listOfData:
        print(i)
    #adds states to database (not incl territoties or DC)
    for i in listOfData:
        if i['state'] == 'AL':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'AK':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'AZ':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'CA':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'CO':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'CT':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'DE':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'FL':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'GA':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'HI':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'ID':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'IA':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'KS':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'KY':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'LA':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'ME':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'MD':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'MA':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'MI':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'MN':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'MS':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'MO':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'MT':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'NE':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'NV':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'NH':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'NJ':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'NM':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'NY':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'NC':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'ND':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'OH':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'OK':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'OR':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'PA':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'RI':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'SC':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'SD':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'TN':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'TX':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'UT':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'VT':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'VA':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'WA':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'WI':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()
        if i['state'] == 'WY':
            my_data = Data(state=i['state'], county=i['county'], vaccineRate=i['metrics']['vaccinationsCompletedRatio'])
            db.session.add(my_data)
            db.session.commit()



if __name__ == "__main__":
    y = getStates()

    app.run(debug=True)