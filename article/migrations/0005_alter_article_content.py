# Generated by Django 3.2.21 on 2023-10-02 13:31

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20231002_1305_squashed_0006_alter_article_entered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=djrichtextfield.models.RichTextField(max_length=20000),
        ),
    ]