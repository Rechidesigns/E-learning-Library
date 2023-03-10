from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    
    STATUS = (("Unpublished","Unpublished"), 
              ("Published","Published"))

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=1200)
    author = models.CharField(max_length=100)
    pages = models.IntegerField(blank=True)
    image = models.ImageField(blank=True)
    file = models.FileField(blank=True)
    price = models.FloatField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    status = models.CharField(max_length= 20, choices=STATUS, default= 'published')
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title