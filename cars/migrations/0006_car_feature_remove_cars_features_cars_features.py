# Generated by Django 4.2 on 2023-05-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_cars_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='cars',
            name='features',
        ),
        migrations.AddField(
            model_name='cars',
            name='features',
            field=models.ManyToManyField(blank=True, to='cars.car_feature'),
        ),
    ]