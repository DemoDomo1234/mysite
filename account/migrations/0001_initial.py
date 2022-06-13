# Generated by Django 4.0.5 on 2022-06-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('familie', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=11)),
                ('is_seller', models.BooleanField(default=False)),
                ('is_special', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('last_login', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]