from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Post page
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs ={'pk':self.pk})

# Games
class Games(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game-detail', kwargs ={'pk':self.pk})

# REVIEWS for game
class Reviews(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='post_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game-detail', kwargs ={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment',null=True,related_name="replies",on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    date_posted =models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))
