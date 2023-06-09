# Generated by Django 4.2 on 2023-06-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Middle_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('serial', models.IntegerField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('re_password', models.CharField(max_length=40)),
                ('textarea', models.CharField(max_length=50)),
                ('Checkbox', models.CharField(max_length=50)),
                ('payments', models.DecimalField(decimal_places=2, max_digits=6)),
                ('django', models.BooleanField()),
            ],
        ),
    ]
