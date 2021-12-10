from django.shortcuts import render, HttpResponse
from .models import NbaMod, NflMod, NcaaMod
from .serializers import NbaSerializer, NflSerializer, NcaaSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from threading import Timer
import json

# Create your views here.

def NbaList(request):
    if request.method == 'GET':
        nbaGames = NbaMod.objects.all()
        serializer = NbaSerializer(nbaGames, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NbaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def NflList(request):
    if request.method == 'GET':
        nflGames = NflMod.objects.all()
        serializer = NflSerializer(nflGames, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NbaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def NcaaList(request):
    if request.method == 'GET':
        ncaaGames = NcaaMod.objects.all()
        serializer = NcaaSerializer(ncaaGames, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NbaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        NcaaMod.delete()
        return HttpResponse(status=204)




def deleteNba():
    games = NbaMod.objects.all()
    for game in games:
        game.delete()
    Timer(30, deleteNba).start()

def deleteNfl():
    games = NflMod.objects.all()
    for game in games:
        game.delete()

    Timer(30, deleteNfl).start()

#
def deleteNcaa():
    games = NcaaMod.objects.all()
    for game in games:
        game.delete()
    Timer(30, deleteNcaa).start()



deleteNcaa()
deleteNba()
deleteNfl()






