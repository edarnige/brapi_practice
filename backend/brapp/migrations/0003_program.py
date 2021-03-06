# Generated by Django 3.1.4 on 2020-12-22 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brapp', '0002_contact_crop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('programDbId', models.TextField(primary_key=True, serialize=False, verbose_name=' programDbId')),
                ('name', models.TextField(verbose_name=' name')),
                ('abbreviation', models.TextField(blank=True, verbose_name=' abbreviation')),
                ('objective', models.TextField(blank=True, verbose_name=' objective')),
                ('leadPerson', models.TextField(blank=True, verbose_name=' leadPerson')),
                ('cropDbId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brapp.crop', verbose_name=' cropDbId')),
            ],
        ),
    ]
