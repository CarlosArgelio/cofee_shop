# Generated by Django 5.0.6 on 2024-07-01 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_author_book_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField()),
                ('biography', models.TextField(max_length=500)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
            ],
        ),
    ]
