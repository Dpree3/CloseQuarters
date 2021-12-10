from bs4 import BeautifulSoup
import requests
import json
from threading import Timer




def nflSchedule():
    html_text = requests.get('https://www.espn.com/nfl/schedule').text

    soup = BeautifulSoup(html_text, 'lxml')

    games = soup.find_all('tr')

    matches = []

    for game in games:
        awayTeam = game.find('a', 'team-name')
        homeTeam = game.find('div', 'home-wrapper')

        if awayTeam != None:
            live = game.find('td', class_='live')
            if live == None:

                continue
            else:
                awayTeam = game.find('a', 'team-name').text
                homeTeam = game.find('div', 'home-wrapper').text




                gettext2 = game.find('td', class_='live').a['href']
                html_text2 = requests.get('https://www.espn.com' + gettext2).text
                soup2 = BeautifulSoup(html_text2, 'lxml')
                quarter = soup2.find('span', class_='status-detail')

                if quarter != None:

                    quarterText = soup2.find('span', class_='status-detail').text
                    awayPoints = soup2.find('div', class_='score icon-font-after').text
                    homePoints = soup2.find('div', class_='score icon-font-before').text

                    if '1st' in quarterText or '2nd' in quarterText:
                        deficit = abs(int(awayPoints) - int(homePoints))
                        if deficit <= 7:
                            gameInfo = f'{awayTeam} at {homeTeam} {awayPoints} to {homePoints} {quarterText} Quarter'
                            matches.append(gameInfo)





    nflDictionaries = []

    nflSchedList = matches

    if len(nflSchedList) == 0:
        contest = {
            "match": 'No Games'
        }
        nflDictionaries.append(contest)

    else:
        for i in nflSchedList:
            contest = {
                "match": i,

            }
            nflDictionaries.append(contest)




    with open("reports/nfl.json", "w") as outfile:
        json.dump(nflDictionaries, outfile)

    Timer(15, nflSchedule).start()





def nbaSchedule():
    matches = []
    html_text = requests.get('https://www.espn.com/nba/schedule').text
    soup = BeautifulSoup(html_text, 'lxml')

    games = soup.find_all('tr')
    for game in games:
        awayTeam = game.find('a', 'team-name')
        homeTeam = game.find('div', 'home-wrapper')

        if awayTeam != None:
            live = game.find('td', class_='live')
            if live == None:
                continue
            else:
                awayTeam = game.find('a', 'team-name').text
                homeTeam = game.find('div', 'home-wrapper').text

                gettext2 = game.find('td', class_='live').a['href']
                html_text2 = requests.get('https://www.espn.com' + gettext2).text
                soup2 = BeautifulSoup(html_text2, 'lxml')
                quarter = soup2.find('span', class_='status-detail')

                if quarter != None:

                    quarterText = soup2.find('span', class_='status-detail').text
                    awayPoints = soup2.find('div', class_='score icon-font-after').text
                    homePoints = soup2.find('div', class_='score icon-font-before').text

                    if '3rd' in quarterText or '4th' in quarterText:
                        deficit = abs(int(awayPoints) - int(homePoints))
                        if deficit <= 7:
                            gameInfo =f'{awayTeam} at {homeTeam} {awayPoints} to {homePoints} {quarterText} Quarter'
                            matches.append(gameInfo)
    nbaDictionaries = []

    nbaSchedList = matches

    if len(nbaSchedList) == 0:
        contest = {
            "match": 'No Games'
        }
        nbaDictionaries.append(contest)

    else:
        for i in nbaSchedList:
            contest = {
                "match": i,

            }
            nbaDictionaries.append(contest)

    with open("reports/nba.json", "w") as outfile:
        json.dump(nbaDictionaries, outfile)

    Timer(15, nbaSchedule).start()





def ncaafSchedule():
    matches = []
    html_text = requests.get('https://www.espn.com/college-football/schedule').text
    soup = BeautifulSoup(html_text, 'lxml')

    games = soup.find_all('tr')
    for game in games:
        awayTeam = game.find('a', 'team-name')
        homeTeam = game.find('div', 'home-wrapper')

        if awayTeam != None:
            live = game.find('td', class_='live')
            if live == None:
                continue
            else:
                awayTeam = game.find('a', 'team-name').text
                homeTeam = game.find('div', 'home-wrapper').text

                gettext2 = game.find('td', class_='live').a['href']
                html_text2 = requests.get('https://www.espn.com' + gettext2).text
                soup2 = BeautifulSoup(html_text2, 'lxml')
                quarter = soup2.find('span', class_='status-detail')

                if quarter != None:

                    quarterText = soup2.find('span', class_='status-detail').text
                    awayPoints = soup2.find('div', class_='score icon-font-after').text
                    homePoints = soup2.find('div', class_='score icon-font-before').text

                    if '1st' in quarterText:
                        deficit = abs(int(awayPoints) - int(homePoints))
                        if deficit <= 7:
                            gameInfo =f'{awayTeam} at {homeTeam} {awayPoints} - {homePoints} {quarterText} Quarter'
                            matches.append(gameInfo)


    ncaaDictionaries = []

    ncaaSchedList = matches

    if len(ncaaSchedList) == 0:
        contest = {
            "match": 'No Games'
        }

        ncaaDictionaries.append(contest)


    else:
        for i in ncaaSchedList:
            contest = {
            "match": i,
        }
            ncaaDictionaries.append(contest)

    with open("reports/ncaa.json", "w") as outfile:
        json.dump(ncaaDictionaries, outfile)

    Timer(15, ncaafSchedule).start()



ncaafSchedule()
nbaSchedule()
nflSchedule()

