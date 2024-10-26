# Generated by Django 5.1 on 2024-10-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='awards',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.JSONField(blank=True, null=True),
        ),
    ]