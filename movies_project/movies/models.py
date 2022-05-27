from django.db import models


class Movie(models.Model):
    title = models.CharField(unique=True, max_length=400)
    year = models.CharField(max_length=20)
    rated = models.CharField(max_length=6)
    released = models.CharField(max_length=40)
    runtime = models.CharField(max_length=15)
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=200)
    writer = models.CharField(max_length=300)
    actors = models.CharField(max_length=400)
    plot = models.TextField()
    language = models.CharField(max_length=30)
    country = models.CharField(max_length=100)
    awards = models.TextField(blank=True, null=True)
    poster = models.CharField(max_length=400, blank=True, null=True)
    ratings = models.CharField(max_length=200)
    metascore = models.CharField(max_length=255)
    imdbRating = models.CharField(max_length=255)
    imdbVotes = models.CharField(max_length=255)
    imdbID = models.CharField(max_length=255)
    type = models.CharField(max_length=15)
    DVD = models.CharField(max_length=255)
    boxOffice = models.CharField(max_length=255)
    production = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
