from django.urls import path
from facts.views import cat_fact, math_gen
urlpatterns = [
    path("", cat_fact, name="home"),
    path("math/", math_gen ,name="math_gen"),
]
