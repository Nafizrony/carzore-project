# Generated by Django 4.2 on 2023-05-02 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='avatar/avatar-11.jpg', null=True, upload_to='photos/%Y/%m/%d/')),
                ('facebook_link', models.URLField(blank=True, max_length=120, null=True)),
                ('twitter_link', models.URLField(blank=True, max_length=120, null=True)),
                ('google_link', models.URLField(blank=True, max_length=120, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]