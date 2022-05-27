from rest_framework import serializers

from .models import Movie, Comment


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title',  'plot', 'poster', 'year', 'genre', 'released', 'actors')


class CommentsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    movie = MovieListSerializer()

    class Meta:
        model = Comment
        fields = ('movie', 'name', 'content', 'created_at')





