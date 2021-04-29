from django.urls import path

from m2m.views import MoviesView, ActorsView

urlpatterns = [
    path('', MoviesView.as_view()),
    path('/actors', ActorsView.as_view())
]