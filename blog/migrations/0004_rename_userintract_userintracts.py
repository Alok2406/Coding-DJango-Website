# Generated by Django 4.0.4 on 2022-08-10 09:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_userintract'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserIntract',
            new_name='UserIntracts',
        ),
    ]
