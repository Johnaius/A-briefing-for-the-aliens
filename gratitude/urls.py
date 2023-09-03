from django.urls import path
from .views import create_thanks


urlpatterns = [
    path("create/", create_thanks, name="create_thanks"),
    # path("upload/", upload, name="upload"),
]