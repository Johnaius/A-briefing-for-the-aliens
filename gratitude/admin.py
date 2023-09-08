from django.contrib import admin
from .models import Gratitude


# Register your models here.
@admin.register(Gratitude)
class GratitudeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        
    )

