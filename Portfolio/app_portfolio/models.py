from distutils.command.upload import upload
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/image')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
