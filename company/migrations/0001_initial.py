# Generated by Django 2.2.1 on 2019-05-06 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('inn', models.CharField(blank=True, max_length=20)),
                ('ogrn', models.CharField(blank=True, max_length=50)),
                ('kpp', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('post_address', models.CharField(blank=True, max_length=300)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('name_director', models.CharField(blank=True, max_length=50)),
                ('post_director', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='company.Company')),
                ('rating', models.BigIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('position', models.ManyToManyField(to='company.Company')),
            ],
        ),
    ]
