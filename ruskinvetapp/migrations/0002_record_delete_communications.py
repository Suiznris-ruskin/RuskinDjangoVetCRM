# Generated by Django 4.2.2 on 2023-07-02 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruskinvetapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=25)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Communications',
        ),
    ]
