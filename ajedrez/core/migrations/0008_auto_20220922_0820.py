# Generated by Django 3.2.9 on 2022-09-22 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_tournamentregistration_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentregistration',
            name='tournament',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.torneo', verbose_name='torneo'),
        ),
        migrations.AlterUniqueTogether(
            name='tournamentregistration',
            unique_together=set(),
        ),
    ]