# Generated by Django 3.2.21 on 2023-10-20 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='product',
        ),
    ]