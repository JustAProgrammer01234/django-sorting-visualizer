from django.shortcuts import render

# Create your views here.
def main(request):
    if 'genarr' in request.GET:
        print('Generating array')
    elif 'bubble' in request.GET:
        print('Sorting array using bubble sort')
    elif 'insertion' in request.GET:
        print('Sorting array using insertion sort')
        
    return render(request, 'visualizer/templates.html')