# Generated by Django 4.1.1 on 2022-09-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('about_project', models.TextField()),
                ('auditory', models.TextField()),
                ('creative', models.TextField()),
                ('advertising', models.TextField()),
                ('site', models.TextField()),
                ('social', models.TextField()),
            ],
        ),
    ]
