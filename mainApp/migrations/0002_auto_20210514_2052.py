# Generated by Django 3.2.2 on 2021-05-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teammate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Birth', models.DateField()),
                ('Nickname', models.CharField(max_length=50)),
                ('Major', models.CharField(max_length=50)),
                ('MBTI', models.CharField(max_length=50)),
                ('Hobby', models.TextField()),
                ('Food', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
