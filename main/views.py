from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("こっぺぱんこっぺぱんこっぺぱんこっぺぱんこっぺぱんこっぺぱんこっぺぱんこっぺぱん")
def hobby(request):
    return HttpResponse("私のhobbyは歩くことかもしれません")
    
def greet(reqest, name):
    message =  "野球しようぜ", name,"お前空気な！"
    return HttpResponse(message)