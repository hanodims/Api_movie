from django.shortcuts import render
import requests
# Create your views here.

def movie_list(request):

    url = 'http://www.omdbapi.com/?apikey=75aab4bb&s=Her'
    response = requests.get(url).json()
    context = {
        'movies' : response
    }
    return render(request, 'list.html', context)

def movie_detail(request, movie_id):

    url = 'http://www.omdbapi.com/?apikey=75aab4bb&i= %s'% movie_id
    response = requests.get(url).json() 

    context = {
    "movie": response
    }
    return render(request, 'detail.html', context)









