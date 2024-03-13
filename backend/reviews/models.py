from django.db import models
from movies.models import Movie
from profiles.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

import uuid


class MovieReview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='reviews')
    movie_list = models.ForeignKey(
        'MovieList', on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField(default=None, blank=True, null=True)
    rating = models.IntegerField(default=None, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ], blank=True, null=True)
    is_favorite = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movie.title} - {self.rating}/10"

    class Meta:
        unique_together = ('movie', 'movie_list')


class MovieList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default="My Movie List")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owners = models.ManyToManyField(Profile, related_name='movie_lists')

    def __str__(self):
        return f"{self.name} - {self.owners.all()}" 

class LikedNotMovie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey("profiles.Profile", on_delete=models.CASCADE, related_name="liked_notmovies")
    category = models.ForeignKey("movies.Category", on_delete=models.CASCADE, related_name="liked_notmovies")
    person = models.ForeignKey("movies.Person", on_delete=models.CASCADE, related_name="liked_notmovies")

    def save(self, *args, **kwargs):
        
        if not (self.category ^ self.person):
            raise ValidationError("Category must be a person or a catergory")
         
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.profile.user.username} - {self.catergory.name if self.catergory.name else self.person.name}"
