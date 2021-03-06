# Generated by Django 3.1.4 on 2020-12-27 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0008_auto_20201227_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('cv', models.FileField(upload_to='apply/')),
                ('cover_letter', models.TextField(max_length=500)),
            ],
        ),
    ]
