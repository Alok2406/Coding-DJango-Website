# Generated by Django 4.0.4 on 2022-08-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_cpost_content_alter_userintract_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpost',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
