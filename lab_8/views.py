from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import os
import json

response = {}



def index(request):
    html = 'lab_8/lab_8.html'

    return render(request, html, response)