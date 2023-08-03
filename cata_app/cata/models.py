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

