# Generated by Django 3.2.4 on 2022-02-07 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='literature',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
