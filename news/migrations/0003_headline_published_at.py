# Generated by Django 3.0.5 on 2020-04-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200418_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='published_at',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
