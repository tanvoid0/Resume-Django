# Generated by Django 2.1.5 on 2019-01-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20190108_0125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-end']},
        ),
        migrations.AlterModelOptions(
            name='fact',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='hobby',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='sub_skill',
            name='category',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='pass_year',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]