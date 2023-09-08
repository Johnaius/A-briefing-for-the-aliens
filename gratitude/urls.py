from django.urls import path
from .views import create_thanks, thanks_list


urlpatterns = [
    path("create/", create_thanks, name="create_thanks"),
    path("list/", thanks_list, name='thanks_list'),
]