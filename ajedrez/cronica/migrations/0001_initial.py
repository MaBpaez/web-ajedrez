# Generated by Django 3.2.9 on 2022-09-12 16:13

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cronica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='titulo')),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('image', models.ImageField(blank=True, upload_to='cronicas', verbose_name='imagen')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='contenido')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha de publicación')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_cronicas', to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('torneo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.torneo')),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
    ]