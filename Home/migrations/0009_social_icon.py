# Generated by Django 2.1.5 on 2019-01-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20190108_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='icon',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]