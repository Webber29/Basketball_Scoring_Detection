# Generated by Django 3.2.12 on 2022-06-07 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videodetail',
            name='pub_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
