import requests
import lxml.html
import time
import random
from SportsCenter import SlackBot
from SportsCenter import FinishedGameInfo
from SportsCenter import BaseballGames

if __name__ == '__main__':
    x = 1


class CurrentGame:
    def __init__(self, teams, scores):
        self.team1 = teams[0]
        self.team2 = teams[1]
        self.score1 = scores[0]
        self.score2 = scores[1]


def checkCurGames():
    gameObjs = [CurrentGame(["", ""], ["", ""])]
    while True:
        url, messageBox = FinishedGameInfo.getUrl('', 'Football')
        doc = lxml.html.fromstring(requests.get(url).content)
        currentGames = doc.xpath('.//div[@class = "game mid-event pre " or @class = "game mid-event pre game-even"]')

        for game in currentGames:
            gameObjs = BaseballGames.curGame(game, gameObjs, './/li[@class = "outcomes total"]/text()',messageBox,
                                             'Football')
        time.sleep(random.randint(120,180))


def gameStarting(teams, scores, quarter, sport):
    message = (teams[0].strip() + " vs " + teams[1].strip() + " has started\n")
    message += (scores[0] + " - " + scores[1] + " --- " + quarter + "\n")
    filler1, messageBox = FinishedGameInfo.getUrl('', sport)
    SlackBot.sendMessage(messageBox, message)

