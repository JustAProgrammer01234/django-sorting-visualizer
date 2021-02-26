import json
import random
from django.shortcuts import render

# Create your views here.
def main(request):

    with open('data.json', 'r') as data:
        information = json.loads(data.read())

    if 'genarr' in request.GET:
        information["array"] = [random.randrange(100,900) for _ in range(284)]

    elif 'bubble' in request.GET:
        information["bubble_sort"] = True
        information["insertion_sort"] = False
        
    elif 'insertion' in request.GET:
        information["bubble_sort"] = False
        information["insertion_sort"] = True
                
    return render(request, 'visualizer/templates.html', {'info': information})   