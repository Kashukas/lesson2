from django.shortcuts import render
from django.http import HttpResponse
from airp_code import ac

# Create your views here.

def airports(request):
    print(request)
    return HttpResponse("<h1>Minsk</h1>")

def airports_home(request):
    #for i, n in ac.items():
    #    aircode = i
    #    cityname = n
    #    tbl = ac
    #    y=list(nd.keys())
        #tbl = {
        #    'aircode': aircode,
        #    'cityname': cityname
        #}
        tbl = ac
        y=list(ac.keys())
        z=list(ac.values())
        return render(request, template_name="homepage.html", context=ac)

def code(request, aircode):
    city = ac.get(aircode.upper(), 'Airport code not found')
    ctx = {
        'city': city
    }
    return render(request, template_name="airports.html", context=ctx)
    # return HttpResponse(ac.get(aircode.upper(), 'Airport code not found'))