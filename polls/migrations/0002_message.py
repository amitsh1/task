# Generated by Django 3.0.7 on 2020-06-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('sender', models.CharField(max_length=200)),
                ('receiver', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
    ]
