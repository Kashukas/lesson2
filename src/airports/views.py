from django.shortcuts import render
from django.http import HttpResponse
from airp_code import ac

# Create your views here.

def airports_home(request): # Homepage.
    return render(request, template_name="homepage.html", context={})


def code(request, aircode): # Return location of airport by code.
    city = ac.get(aircode.upper(), 'Airport code not found')
    ctx = {'city': city}
    return render(request, template_name="airports.html", context=ctx)