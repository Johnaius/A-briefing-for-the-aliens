from django.urls import path
from facts.views import cat_fact, math_gen
urlpatterns = [
    path("cat", cat_fact, name="cat_fact"),
    path("math/", math_gen ,name="math_gen"),
]
