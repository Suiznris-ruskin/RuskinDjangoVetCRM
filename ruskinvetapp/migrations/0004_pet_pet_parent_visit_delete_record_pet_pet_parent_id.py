# Generated by Django 4.2.2 on 2023-07-04 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ruskinvetapp', '0003_communications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATED_DT', models.DateTimeField(auto_now_add=True)),
                ('NAME', models.CharField(max_length=50)),
                ('GENDER', models.CharField(max_length=10)),
                ('SPECIES', models.CharField(max_length=25)),
                ('BREED', models.CharField(choices=[('CANINE', 'Dog'), ('FELINE', 'Cat')], max_length=50)),
                ('COLOR', models.CharField(choices=[('ALBINO', 'Albino'), ('AMBER', 'Amber'), ('APRICOT', 'Apricot'), ('BEIGE', 'Beige'), ('BLACK', 'Black'), ('BLONDE', 'Blonde'), ('BROWN', 'Brown'), ('PEACH', 'Peach'), ('YELLOW', 'Yellow'), ('WHITE', 'White')], max_length=15)),
                ('NOTES', models.TextField()),
                ('DATE_OF_BIRTH', models.DateField()),
                ('WEIGHT', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet_Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATED_AT', models.DateTimeField(auto_now_add=True)),
                ('FIRST_NAME', models.CharField(max_length=50)),
                ('LAST_NAME', models.CharField(max_length=50)),
                ('DATE_OF_BIRTH', models.DateField()),
                ('EMAIL', models.CharField(max_length=100)),
                ('GENDER', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('NONBINARY', 'Non Binary')], max_length=15)),
                ('PHONE', models.CharField(max_length=15)),
                ('ADDRESS', models.CharField(max_length=100)),
                ('CITY', models.CharField(max_length=50)),
                ('STATE', models.CharField(max_length=25)),
                ('ZIPCODE', models.CharField(max_length=10)),
                ('CONTACT_METHOD', models.CharField(choices=[('PHONE', 'Phone'), ('EMAIL', 'Email')], max_length=15)),
                ('CONTACT_TYPE', models.CharField(choices=[('CUSTOMER', 'Customer'), ('VET', 'Veterinarian'), ('STAFF', 'Staff Member'), ('SUPPLIER', 'Supplier Contact'), ('SYNDICATE', 'Syndicate Contact'), ('PHARMACY', 'Pharmacy')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATED_AT', models.DateTimeField(auto_now_add=True)),
                ('REASON', models.CharField(max_length=250)),
                ('DATE_OF_VISIT', models.DateTimeField(auto_now_add=True)),
                ('PET_ID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='ruskinvetapp.pet')),
                ('PET_PARENT_ID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='ruskinvetapp.pet_parent')),
            ],
        ),
        migrations.DeleteModel(
            name='Record',
        ),
        migrations.AddField(
            model_name='pet',
            name='PET_PARENT_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='ruskinvetapp.pet_parent', verbose_name='Series'),
        ),
    ]