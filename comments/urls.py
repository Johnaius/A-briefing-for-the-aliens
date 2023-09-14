from django.urls import path
from comments.views import create_comment

urlpatterns = [
    path("create/", create_comment, name="create_comment"),
]