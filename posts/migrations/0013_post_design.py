# Generated by Django 4.1 on 2022-08-25 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_post_design_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='design',
            field=models.BooleanField(default='False'),
        ),
    ]
