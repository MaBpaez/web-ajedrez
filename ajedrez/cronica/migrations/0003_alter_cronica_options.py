# Generated by Django 3.2.9 on 2022-09-16 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cronica', '0002_alter_cronica_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cronica',
            options={'ordering': ['-publish'], 'verbose_name_plural': 'crónicas'},
        ),
    ]