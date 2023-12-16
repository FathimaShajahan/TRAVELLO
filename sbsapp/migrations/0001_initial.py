# Generated by Django 4.2.6 on 2023-10-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('country', models.TextField()),
            ],
        ),
    ]
