# Generated by Django 4.1 on 2022-08-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_schedule_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='design_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
