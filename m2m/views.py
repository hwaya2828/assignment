import json

from django.http import JsonResponse
from django.views import View
from m2m.models import Movie, Actor

# Create your views here.

class MoviesView(View):
    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(
            title = data['title'],
            release_date = data['release_date'],
            running_time = data['running_time']
        )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request):
        movies = Movie.objects.all()
        actors = Actor.objects.all()
        results = []
        for movie in movies:
            total_actor = []
            for actor in actors:
                for actor_movie in actor.movies.all():
                    if actor_movie.title == movie.title:
                        total_actor.append(
                            {
                                "actor's name" : actor.first_name
                            }
                        )
            results.append(
                {
                    "title" : movie.title,
                    "running_time" : movie.running_time,
                    "actor(s)" : total_actor
                }
        )
        return JsonResponse({'resutls':results}, status=200)


class ActorsView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            date_of_birth = data['date_of_birth']
        )
        actor = Actor.objects.get(first_name=data['first_name'])
        movie = Movie.objects.get(title=data['movies'])
        actor.movies.add(movie)
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request):
        actors = Actor.objects.all()
        results  = []
        for actor in actors:
            total_movie = []
            for movie in actor.movies.all():
                total_movie.append(
                    {
                        "movie(s)'s title" : movie.title
                    }
                )
            results.append(
                {
                    "first_name" : actor.first_name,
                    "last_name" : actor.last_name,
                    "movie(s)" : total_movie
                }
            )
        return JsonResponse({'resutls':results}, status=200)