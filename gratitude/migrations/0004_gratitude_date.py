# Generated by Django 4.2.4 on 2023-09-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gratitude', '0003_gratitude_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='gratitude',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]