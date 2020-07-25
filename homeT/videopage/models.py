from django.db import models

# Create your models here.

class Post(models.Model):
    url = models.TextField()
    hashtags = models.ManyToManyField('Hashtag', blank = True)
    hashtagBox = models.TextField('HashtagBox', blank = True)

    def __str__(self):
        return self.url

class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content

class Reviews(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    reviews_textfield = models.TextField()