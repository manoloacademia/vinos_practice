# Generated by Django 3.2.5 on 2022-08-03 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_cellar_winery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wine',
            old_name='cellar',
            new_name='winery',
        ),
    ]
