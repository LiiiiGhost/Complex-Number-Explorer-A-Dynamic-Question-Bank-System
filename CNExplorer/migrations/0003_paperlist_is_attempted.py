# Generated by Django 4.0.2 on 2022-03-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CNExplorer', '0002_questiondatabase'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperlist',
            name='is_attempted',
            field=models.CharField(default='', max_length=32, verbose_name='paperstatus'),
        ),
    ]
