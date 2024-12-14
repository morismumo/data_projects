#script to fetch the healthcare data 

import requests

# Now to fetch and load data as json
url = 'our data source api url'
def fetch_and_load_data(url):
    response = requests.get('url')
    #let's check if response is a success -- then load the data to json
    if response.status_code == 200:
        data = response.json()
    else:
        print('failed: ', response.status_code)



