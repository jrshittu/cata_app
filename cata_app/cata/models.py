from django.db import models

# Create your models here.
class Publisher(models.Model):
    publisher_name = models.CharField("Publisher's Name", max_length=200)

def __str__(self):
    return self.publisher_name

class Publication(models.Model):
    type_choices = [('NEWSPAPER', 'Newspaper'), ('MAGAZINE', 'Magazine')]
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True)
    publication_name = models.CharField("Publication Name", max_length=200)
    publication_notes = models.CharField("Publication Notes", max_length=200, blank=True)
    publication_type = models.CharField("Publication Type", max_length=200, choices=type_choices)

class Article(models.Model):
    title = models.CharField(max_length=200)
    article_id = models.BigAutoField(primary_key=True)
    keywords = models.TextField(default=0)
    
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_id = models.BigAutoField(primary_key=True)
    
class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    tag_id = models.BigAutoField(primary_key=True)

class Edition(models.Model):
    edition_name = models.CharField(max_length=200)
    edition_id = models.BigAutoField(primary_key=True)
