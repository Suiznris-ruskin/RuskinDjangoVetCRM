# Generated by Django 4.2.2 on 2023-07-07 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruskinvetapp', '0006_rename_breed_pet_breed_rename_color_pet_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='assessment',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='assessment_ai',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='check_me_out',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='visit',
            name='diagnosis',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='diagnosis_ai',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='history',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='meds_suppl',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='mucus_membrane',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='mucus_mentation',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='problem_list',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='problem_list_ai',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='prognosis',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='prognosis_ai',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='pulse',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='respiratory_rate',
            field=models.CharField(choices=[('LOW', '<15'), ('NORMAL', '15-30'), ('HIGH', '>30')], default='15-30', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='second_tag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='visit',
            name='temperature',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='weight',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='weight_unit',
            field=models.CharField(choices=[('KG', 'kg'), ('LBS', 'lbs')], default='kg', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='exam_room',
            field=models.CharField(choices=[('ROOM1', 'Exam Room 1'), ('ROOM2', 'Exam Room 2'), ('ROOM3', 'Exam Room 3'), ('ROOM4', 'Exam Room 4'), ('ROOM5', 'Exam Room 5'), ('ROOM6', 'Exam Room 6'), ('ROOM7', 'Exam Room 7'), ('ROOM8', 'Exam Room 8')], default='Exam Room 1', max_length=15, null=True),
        ),
    ]