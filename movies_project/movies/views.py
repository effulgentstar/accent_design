import traceback

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Movie, Comment
from .forms import CommentForm, SearchForm
import requests
from .serializer import CommentsSerializer, MovieListSerializer

API_KEY = '5cfd4baf'


@api_view(['GET'])
def get_movies(request):
    form = SearchForm()
    movies = Movie.objects.all().order_by('title')
    serializer = MovieListSerializer(movies, many=True)
    context = {"title": "All Movies",
               "form": form,
               "all_movies": serializer.data}
    return render(request, 'movies/all_movies.html', context)


@api_view(['POST'])
def add_movie(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        title = data['title']
        movies = Movie.objects.filter(title__contains=title)
        if movies:
            serializer = MovieListSerializer(movies, many=True)
            context = {"form": SearchForm(),
                       "all_movies": serializer.data}
            return render(request, 'movies/all_movies.html', context)
        try:
            url = f'http://www.omdbapi.com/?t={title}&apikey={API_KEY}'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        data = response.json()
        if data['Response'] == "True":
            movie_data = Movie(
                title=data['Title'],
                year=data['Year'],
                rated=data['Rated'],
                released=data['Released'],
                runtime=data['Runtime'],
                genre=data['Genre'],
                director=data['Director'],
                writer=data['Writer'],
                actors=data['Actors'],
                plot=data['Plot'],
                language=data['Language'],
                country=data['Country'],
                awards=data['Awards'],
                poster=data['Poster'],
                ratings=data['Ratings'],
                metascore=data['Metascore'],
                imdbRating=data['imdbRating'],
                imdbVotes=data['imdbVotes'],
                imdbID=data['imdbID'],
                type=data['Type'], )

            movie_data.save()
            context = {"form": SearchForm(),
                       "all_movies": movie_data}
            return render(request, 'movies/all_movies.html', context)
        else:
            raise Http404("No Movie matches the given query")


@api_view(['GET', 'POST'])
def add_comment(request, movie_id):
    form = CommentForm()
    movie = Movie.objects.get(id=movie_id)
    movie_serializer = MovieListSerializer(movie)
    comment = {}
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            comment = data['comment']
            new_comment = Comment.objects.create(movie=movie, name=name, content=comment)
            comment = CommentsSerializer(new_comment).data
            form = CommentForm()
    context = {
        "form": form,
        'movie': movie_serializer.data,
        'comment': comment
    }
    return render(request, 'movies/movie_detail.html', context)


@api_view(['GET'])
def get_comments(request):
    form = SearchForm(request.GET)
    comments = Comment.objects.all()
    if form.is_valid():
        data = form.cleaned_data
        title = data['title']
        try:
            movie = Movie.objects.filter(title__contains=title).first()
            serializer = MovieListSerializer(movie)
            movie_id = serializer.data['id']
            comments = comments.filter(movie_id__in=[int(movie_id)])

        except:
            raise Http404("No Movie matches the given query")

    comment_serializer = CommentsSerializer(comments.order_by('-created_at'), many=True)
    context = {"title": "All comments",
               "form": SearchForm(),
               'comments': comment_serializer.data}
    return render(request, 'movies/all_comments.html', context)

