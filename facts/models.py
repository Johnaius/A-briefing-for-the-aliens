from django.db import models

class MathProblem(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    answer = models.IntegerField()
    user_response = models.IntegerField(null=True, blank=True)