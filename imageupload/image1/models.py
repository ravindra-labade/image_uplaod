from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return f'{self.title}'
