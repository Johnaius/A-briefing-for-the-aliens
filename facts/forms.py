from django import forms
from .models import MathProblem

class MathProblemForm(forms.ModelForm):
    class Meta:
        model = MathProblem
        fields = ['user_response']