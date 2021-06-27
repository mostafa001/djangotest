# Generated by Django 2.1.5 on 2021-06-27 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmanagement', '0003_auto_20210627_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=60, null=True)),
                ('items', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.CharField(blank=True, max_length=60, null=True)),
                ('quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
