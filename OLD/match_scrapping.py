import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

link = r'scrapping\teams_info_all_seasons.csv'
data_ext = pd.read_csv(link)

x = data_ext.shape[0]
stats = []
request_counter = 0

for i in range(0,2):
    url = data_ext['club_link'][i]
    print("Scraping of ", url)

    response = requests.get(url)
    request_counter += 1

    if request_counter > 10:
        print("Reached request limit. Sleeping for 60 seconds...")
        time.sleep(60)  
        request_counter = 0  

    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')

    data = {
            'player': soup.find_all('table', {'id' : 'stats_standard_12'}, 'tbody', 'tr', 'th', {'data-stat': 'player'})
    }

    print(data)

