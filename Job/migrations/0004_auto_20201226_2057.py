# Generated by Django 3.1.4 on 2020-12-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0003_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='Vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
