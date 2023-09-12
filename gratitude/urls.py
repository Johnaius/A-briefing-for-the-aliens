from django.urls import path
from .views import create_thanks, thanks_list, my_list, home, show_detail, thanks_delete


urlpatterns = [
    path("", home, name="home"),
    path("create/", create_thanks, name="create_thanks"),
    path("list/", thanks_list, name='thanks_list'),
    path("mine/", my_list, name='my_list'),
    path("<int:id>/", show_detail, name='show_detail'),
     path("<int:id>/delete/", thanks_delete, name='thanks_delete'),
]