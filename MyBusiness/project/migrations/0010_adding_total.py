# Generated by Django 3.0.4 on 2020-04-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20200408_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='adding',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]