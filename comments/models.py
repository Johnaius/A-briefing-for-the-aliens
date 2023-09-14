from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    comments = models.TextField(max_length=200)
    date = models.DateField(default=timezone.now, null=True)
    gratitude = models.ForeignKey(
        "gratitude.Gratitude",
        related_name="comments",
        on_delete=models.CASCADE,
        null=True
        
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comments",
        on_delete=models.CASCADE,
        null=True
    )