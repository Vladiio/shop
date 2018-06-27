from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=60)


class Book(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='books')
    title = models.CharField(max_length=60)
    price = models.PositiveIntegerField()
