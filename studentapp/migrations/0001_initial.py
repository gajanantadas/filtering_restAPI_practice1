# Generated by Django 3.1.6 on 2021-02-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('passby', models.FloatField()),
            ],
        ),
    ]
