from django.db import models


class Topic(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=63, verbose_name='Name')
    slug = models.SlugField(max_length=63, unique=True, verbose_name='Slug')

    def __str__(self):
        return str(self.name)


class Workshop(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, default='', blank=True)
    description = models.TextField(default='', blank=True)
    topics = models.ManyToManyField(Topic, blank=True)

    def __str__(self):
        return str(self.name)