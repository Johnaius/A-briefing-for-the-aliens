from django.db import models
from django.conf import settings


# Create your models here.
class Gratitude(models.Model):
    title = models.CharField(max_length=50, null=True)
    one = models.CharField(max_length=150)
    two = models.CharField(max_length=150)
    three = models.CharField(max_length=150)
    four = models.TextField()
    image = models.ImageField(upload_to='static/images/')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="thanks",
        on_delete=models.CASCADE,
        null=True,
    )
    

    def __str__(self):
        return self.title


  



