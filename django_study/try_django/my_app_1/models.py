from django.db import models

# Create your models here.
class Author(models.Model):
    # id = models.AutoField
    name = models.CharField(max_length = 100)
    birthdate = models.DateField(blank = True, null = True)

    def __str__(self):
        return 'Author: ', self.name

    # class Meta:
    #     plural_name = 'books'
    #     db_table = 'books20'

class Book(models.Model):
    title = models.CharField(max_length = 100)
    isbn = models.CharField(max_length = 100, unique = True)
    authrs = models.ManyToManyField(to = Author)
    slug = models.SlugField()