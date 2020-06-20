import requests
import json
import pandas as pd

class Data:

    def __init__(self):
        self.countrydata = []
        self.statedata = []
        self.districtdata = []

    def get_country_data(self):
        URL_country_data = 'https://api.covid19india.org/data.json'
        country_data = requests.get(URL_country_data).text
        country = json.loads(country_data)
        df = pd.json_normalize(country['cases_time_series'])
        self.countrydata = pd.DataFrame(df)
        return self.countrydata

    def get_state_data(self):
        URL_state_data = 'https://api.covid19india.org/data.json'
        state_data = requests.get(URL_state_data).text
        states = json.loads(state_data)
        self.statedata = pd.json_normalize(states['statewise'])
        return self.statedata

    def get_district_data(self, state_name):
        URL_district_data = 'https://api.covid19india.org/v2/state_district_wise.json'
        district_data = requests.get(URL_district_data).text
        districts = json.loads(district_data)
        for content in districts:
            if state_name.lower() == content['state'].lower():
                self.districtdata = pd.json_normalize(content['districtData'])
        return self.districtdata
