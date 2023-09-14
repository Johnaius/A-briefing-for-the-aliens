# Generated by Django 4.2.4 on 2023-09-14 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gratitude', '0004_gratitude_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0006_alter_comment_date_alter_comment_gratitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='gratitude',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='gratitude.gratitude'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
