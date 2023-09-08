from django.forms import ModelForm
from .models import Gratitude

class GratitudeForm(ModelForm):
    class Meta:
        model=Gratitude
        fields =(
            'title',
            'one',
            'two',
            'three',
            'four',
            'five',
            'image',
        )


    


        #  'One Word to describe the day',
        #     'How were you Challenged today?',
        #     'Three things to work on',
        #     'Who did you interact with today',
        #     'One thing you accomplished today',
        #     'Say a positive affirmation here',