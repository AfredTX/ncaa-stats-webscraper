#!/usr/bin/env python3
"""
Python webscrapping module.

Webscrap teamrankings.com website to obtain a list of the top 68 basketball
teams and url references to use for webscrapping other websites for team stats.
"""
from itertools import islice

import requests
from bs4 import BeautifulSoup

# assign url to variable and use requests to get html
url = 'https://www.teamrankings.com/ncb/'
teams_page = requests.get(url)
teams = teams_page.content

# parse html with BeautifulSoup
soup = BeautifulSoup(teams, 'html.parser')

# scrap all team names and add to a dictionary
full_teams_list = {}
lst = soup.find_all('div', {'class': 'table-team-logo-text'})
for item in lst:
    team_name = item.find('a').text
    # scrap url reference for team name (e.g., 'gonzaga-bulldogs')
    url_ref = item.find('a')['href'][22:]
    full_teams_list[team_name] = url_ref


def take(n, iterable):
    """Return first n items of the iterable as a list."""
    return list(islice(iterable, n))


# grab top 68 teams and create list of teams and list of url references
top_68 = take(68, full_teams_list.items())
teams_list = []
url_ref_list = []
for tup in top_68:
    teams_list.append(tup[0])
    url_ref_list.append(tup[1])

# build two lists of urls to scrap stats for each team
stat_url_list = []
sos_url_list = []
for url in url_ref_list:
    stat_url_list.append('https://www.teamrankings.com/ncaa-basketball/team/' +
                         url + '/stats')
    sos_url_list.append('https://www.teamrankings.com/ncaa-basketball/team/' +
                        url + '/rankings')
