from django.shortcuts import render

# Create your views here.
response = {'author' : 'Anisha Inas'} 

def index(request):
	html = 'lab_6/lab_6.html'
	return render(request, html, response)