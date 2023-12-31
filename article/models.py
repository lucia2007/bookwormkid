from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField


STATUS = ((0, "Draft"), (1, "Published"))


class Article(models.Model):
    """ Model for creating/managing articles """
    title = models.CharField(max_length=254, unique=True)
    entered_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='article_posts',
        default=1
        )
    author = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    image_description = models.CharField(
        max_length=100, default="no description provided"
        )
    content = RichTextField(max_length=20000)
    excerpt = models.TextField(max_length=254, blank=True)
    likes = models.ManyToManyField(
        User, related_name='article_likes', blank=True
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=254, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    source = models.CharField(max_length=500)

    class Meta:
        """ Order articles from newest to oldest """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
