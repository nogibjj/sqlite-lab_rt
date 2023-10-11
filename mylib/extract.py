import requests

def extract(url="https://github.com/nickeubank/MIDS_Data/raw/master/US_AmericanCommunitySurvey/US_ACS_2017_10pct_sample.dta", 
            file_path="american_community_survey.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



