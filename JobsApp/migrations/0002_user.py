# Generated by Django 3.2.4 on 2022-11-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=101)),
                ('password', models.CharField(max_length=43)),
            ],
        ),
    ]
