from django.db import models
import json

from threading import Timer

class NbaMod(models.Model):
    match = models.CharField(max_length=100)

    @classmethod
    def create(cls, match):
        game = cls(match=match)
        return game


    def __str__(self):
        return self.match



class NflMod(models.Model):
    match = models.CharField(max_length=100)

    @classmethod
    def create(cls, match):
        game = cls(match=match)
        return game

    def __str__(self):
        return self.match


class NcaaMod(models.Model):
    match = models.CharField(max_length=100)

    @classmethod
    def create(cls, match):
        game = cls(match=match)
        return game


    def __str__(self):
        return self.match

#
def addNba():
    gameAmount = NbaMod.objects.count()
    if gameAmount == 0:
        path = '/Users/deshawnprewitt/PycharmProjects/pythonProject/closeappbackend/CloseWebScraper/reports/nba.json'
        text = open(path)
        loadText = json.load(text)

        for match in loadText:
            game = NbaMod.create(match['match'])
            game.save()

    Timer(2, addNba).start()


def addNfl():
    gameAmount = NflMod.objects.count()
    if gameAmount == 0:
        path = '/Users/deshawnprewitt/PycharmProjects/pythonProject/closeappbackend/CloseWebScraper/reports/nfl.json'
        text = open(path)
        loadText = json.load(text)

        for match in loadText:
            game = NflMod.create(match['match'])
            game.save()

    Timer(2, addNfl).start()

def addNcaa():
    gameAmount = NcaaMod.objects.count()
    if gameAmount == 0:
        path = '/Users/deshawnprewitt/PycharmProjects/pythonProject/closeappbackend/CloseWebScraper/reports/ncaa.json'
        text = open(path)
        loadText = json.load(text)

        for match in loadText:
            game = NcaaMod.create(match['match'])
            game.save()

    Timer(2, addNcaa).start()

addNcaa()
addNba()
addNfl()
# Create your models here.
