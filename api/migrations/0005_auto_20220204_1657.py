# Generated by Django 3.1 on 2022-02-04 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211221_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-quentity'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
