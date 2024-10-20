import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define league and seasons
leagues = {
    'Premier League': 'https://fbref.com/en/comps/9/',
    'Bundesliga': 'https://fbref.com/en/comps/20/',
    'La Liga': 'https://fbref.com/en/comps/12/',
    'Serie A': 'https://fbref.com/en/comps/11/',
    'Ligue 1': 'https://fbref.com/en/comps/13/'
}

# List to hold the years from 2010 to the current year
current_year = 2024  # Change this to the current year
seasons = [f"{year}-{year + 1}" for year in range(2010, current_year + 1)]

# Initialize a list to hold team data
clubs = []

# Loop through each league and each season
for league_name, base_url in leagues.items():
    for season in seasons:
        url = f"{base_url}{season}/{season}-{league_name.replace(' ', '-')}-Stats"
        print(f"Scraping {league_name} for the season {season}...")

        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to retrieve data for {league_name} in the season {season}. Status code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <th> tags with data-stat="team"
        team_cells = soup.find_all('th', {'data-stat': 'team'})

        # Check if any team cells were found
        if not team_cells:
            print(f"No team cells found for {league_name} in the season {season}.")
            continue

        # Iterate over the found team cells and extract data
        for team_cell in team_cells:
            club_link_tag = team_cell.find('a')  # Find the <a> tag within the team cell
            if club_link_tag:
                club_name = club_link_tag.text.strip()  # Get the club name
                club_link = 'https://fbref.com' + club_link_tag['href']  # Get the full club URL

                # Check if the link already exists in the clubs list
                if not any(club['club_link'] == club_link for club in clubs):
                    clubs.append({
                        'club_name': club_name,
                        'club_link': club_link,
                        'season': season  # Add season for context
                    })
                else:
                    print(f"Duplicate link found: {club_link} for {club_name} in season {season}")  # Debugging message for duplicates
            else:
                print(f"No link found for team: {team_cell.text.strip()}")  # Debugging message for missing links

# Create a DataFrame and save to CSV
df = pd.DataFrame(clubs)
df.to_csv('teams_info_all_seasons.csv', index=False)

print("Team URLs scraped and saved to teams_info_all_seasons.csv")
