import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

leagues = {
    'Premier League': 'https://fbref.com/en/comps/9/',
    'Bundesliga': 'https://fbref.com/en/comps/20/',
    'La Liga': 'https://fbref.com/en/comps/12/',
    'Serie A': 'https://fbref.com/en/comps/11/',
    'Ligue 1': 'https://fbref.com/en/comps/13/'
}

current_year = 2024  
seasons = [f"{year}-{year + 1}" for year in range(2022, current_year + 1)] 
request_counter = 0 
results = []

for league_name, base_url in leagues.items():
    for season in seasons:
        
        url = f"{base_url}{season}/calendrier/Calendrier-et-resultats-{season}-{league_name.replace(' ', '-')}"
        print(f"Scraping {league_name} for the season {season}...")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }
        
        response = requests.get(url)
        request_counter += 1
        
        if request_counter > 10:
            print("Reached request limit. Sleeping for 60 seconds...")
            time.sleep(60)  
            request_counter = 0  

        if response.status_code != 200:
            print(f"Failed to retrieve data for {league_name} in the season {season}. Status code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        data = {
            'game-week': soup.find_all('th', {'data-stat': 'gameweek'}),
            'day-of-week': soup.find_all('td', {'data-stat': 'dayofweek'}),
            'date' : soup.find_all('td', {'data-stat': 'date'}),
            'start-time' : soup.find_all('td', {'data-stat': 'start_time'}),
            'home-team' : soup.find_all('td', {'data-stat': 'home_team'}),
            'home-xg' : soup.find_all('td', {'data-stat': 'home_xg'}),
            'score': soup.find_all('td', {'data-stat' : 'score'}),
            'away-xg': soup.find_all('td', {'data-stat' : 'away_xg'}),
            'away-team': soup.find_all('td', {'data-stat' : 'away_team'}),
            'attendance': soup.find_all('td', {'data-stat' : 'attendance'}),
            'venue': soup.find_all('td', {'data-stat' : 'venue'})
        }
        del data["game-week"][0]

        x = min(len(col) for col in data.values())

        for i in range(0,x):
            league = league_name 
            game_week = data['game-week'][i].text.strip()
            day_of_week = data['day-of-week'][i].text.strip()
            start_time = data['start-time'][i].text.strip()
            home_team = data['home-team'][i].text.strip()
            score = data['score'][i].text.strip()
            print(score)
            away_team = data['away-team'][i].text.strip()
            attendance = data['attendance'][i].text.strip()
            venue = data['venue'][i].text.strip()
            date_find = data['date'][i].find('a')

            if date_find:
                print("X")
                game_date = date_find.text.strip()
                
                if game_week == "" or  day_of_week == "":
                    break

                if data['home-xg'][i].text.strip() != "":
                    print("X")
                    home_xg = data['home-xg'][i].text.strip()
                    away_xg = data['away-xg'][i].text.strip()
                    
                else:
                    print("X")
                    home_xg = "X"
                    away_xg = "X"  
                
                results.append({
                    'league': league,
                    'season': season,
                    'game-week': game_week,
                    'day-of-week': day_of_week,
                    'date' : game_date,
                    'start-time' : start_time,
                    'home-team' : home_team,
                    'home-xg' : home_xg,
                    'score' : score,
                    'away-xg' : away_xg,
                    'away-team' : away_team,
                    'attendance' : attendance,
                    'venue' : venue
                    })

df = pd.DataFrame(results)
df.to_csv('teams_results_all_seasons.csv', index=False)

print("Team results scraped and saved to teams-results_all_seasons.csv")