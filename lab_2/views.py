from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

#TODO Implement
#Create a content paragraph for your landing page:
landing_page_content = 'I am a princess cut from marble, smoother than a storm. \
						And the scars that mark my body, they are silver and gold. \
						My blood is a flood of rubies, precious stones. \
						It keeps my veins hot, the fire has found a home in me.\
						I move through town, I’m quiet like a fight. \
						And my necklace is of rope, I tie it and untie it'

def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'index_lab2.html', response)