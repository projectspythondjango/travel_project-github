# Generated by Django 4.1.6 on 2023-02-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pic', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Table2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
