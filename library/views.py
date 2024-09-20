from django.shortcuts import render
from django.http import HttpResponse
from ninja import NinjaAPI

api= NinjaAPI()


def home(request):
    return HttpResponse("Welcome to the Library Management System!")
