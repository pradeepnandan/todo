# Generated by Django 5.0 on 2023-12-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('priority', models.CharField(max_length=250)),
                ('remarks', models.CharField(max_length=250)),
            ],
        ),
    ]
