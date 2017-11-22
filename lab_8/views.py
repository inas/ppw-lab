from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import os
import json

response = {}



def index(request):
    response['author'] = 'Anisha Inas'
    html = 'lab_8/lab_8.html'
    return render(request, html, response)

def profile(request):
    html = 'lab_8/profile.html'
    return render(request, html, response)