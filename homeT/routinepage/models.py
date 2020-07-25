from django.db import models
from django.conf import settings

# Create your models here.

class Routine(models.Model):
    WORKOUT_PART =(
        ('하체','하체'),
        ('상체','상체'),
        ('복근','복근'),
    )
    title = models.CharField(max_length=200)

    url1 = models.CharField(max_length=500)
    part1 = models.CharField(max_length=2, choices=WORKOUT_PART, default='하체')

    url2 = models.CharField(max_length=500)
    part2 = models.CharField(max_length=2, choices=WORKOUT_PART, default='상체')

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    routine_id = models.ForeignKey(Routine, on_delete=models.CASCADE)