from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Gratitude(models.Model):
    title = models.CharField(max_length=50, null=True)
    one = models.CharField(max_length=150)
    two = models.CharField(max_length=150)
    three = models.CharField(max_length=150)
    four = models.CharField(max_length=150)
    five = models.CharField(max_length=150)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title


  

# @property
# def image_url(self):
#     return (
#         f"https://res.cloudinary.com/johnaius/{self.image}"
#     )


