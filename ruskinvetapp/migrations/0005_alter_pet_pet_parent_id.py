# Generated by Django 4.2.2 on 2023-07-04 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ruskinvetapp', '0004_pet_pet_parent_visit_delete_record_pet_pet_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='PET_PARENT_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='ruskinvetapp.pet_parent'),
        ),
    ]
