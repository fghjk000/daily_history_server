# Generated by Django 5.0.3 on 2024-03-20 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('detail', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.TextField(verbose_name='그림')),
                ('contents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily_history.contents')),
            ],
        ),
    ]