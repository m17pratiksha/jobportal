# Generated by Django 3.1.6 on 2021-02-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField(max_length=100)),
                ('file', models.FileField(null=True, upload_to='files/', verbose_name='')),
            ],
        ),
    ]
