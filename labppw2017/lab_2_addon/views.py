# Create your views here.
from django.shortcuts import render
from lab_1.views import mhs_name, birth_date
#Create a list of biodata that you wanna show on webpage:
#[{'subject' : 'Name', 'value' : 'Igor'},{{'subject' : 'Birth Date', 'value' : '11 August 1970'},{{'subject' : 'Sex', 'value' : 'Male'}
#TODO Implement
bio_dict = [{'subject' : 'Name', 'value' : mhs_name},\
{'subject' : 'Birth Date', 'value' : '6 May 1999'},\
{'subject' : 'Sex', 'value' : 'Female'}]

def index(request):
    response = {}
    return render(request, 'description_lab2addon.html', response)
