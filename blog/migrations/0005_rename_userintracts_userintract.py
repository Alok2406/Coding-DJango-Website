# Generated by Django 4.0.4 on 2022-08-10 09:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_rename_userintract_userintracts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserIntracts',
            new_name='UserIntract',
        ),
    ]
