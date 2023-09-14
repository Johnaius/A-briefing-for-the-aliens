from django.forms import ModelForm
from comments.models import Comment


class CommentsForm(ModelForm):
    class Meta:
        model = Comment
        fields = (
            "comments",
            "gratitude"
            
        )
