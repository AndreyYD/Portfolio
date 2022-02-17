from django.db import models


class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    image = models.ImageField(upload_to='blog/image', blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title
