# Generated by Django 3.2.21 on 2023-10-02 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0005_alter_article_entered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='entered_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='article_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
