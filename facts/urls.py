from django.urls import path
from facts.views import cat_fact

urlpatterns = [
    path("", cat_fact, name="home")
]