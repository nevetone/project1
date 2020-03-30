# Generated by Django 3.0.3 on 2020-03-09 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nowosci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=60)),
                ('opis', models.TextField()),
                ('data', models.DateField()),
                ('glowny', models.BooleanField()),
                ('autor', models.CharField(max_length=20)),
                ('CzyMaPodStrone', models.BooleanField()),
                ('link', models.CharField(blank=True, default='Jeżeli ma podstronę wpisz Tytuł bez spacji', max_length=200, null=True)),
                ('CzyMaZdjecie', models.BooleanField()),
                ('nazwaZdj', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
