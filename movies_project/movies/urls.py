
from django.urls import  path

from movies import views

urlpatterns = [
    path('', views.get_movies, name="get_movies"),
    path('add-movie', views.add_movie, name="add_movie"),
    path('<int:movie_id>/add-comment', views.add_comment, name="add_comment"),
    path('get-comments', views.get_comments, name="get_comments"),
]
