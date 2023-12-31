# Generated by Django 4.2.7 on 2023-11-09 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('groups', '0001_initial'),
        ('accoounts', '0001_initial'),
        ('speciality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_type', models.CharField(max_length=10)),
                ('classroom_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_time', models.CharField(choices=[('1', '08:30-10:00'), ('2', '10:00-11:30'), ('3', '11:30-13:00'), ('4', '13:00-14:30'), ('5', '14:30-16:00')], max_length=20)),
                ('session_type', models.CharField(choices=[('TD', 'TD'), ('TP', 'TP'), ('COUR', 'COUR')], max_length=5)),
                ('session_date', models.DateField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classrooms.classroom')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accoounts.professor')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speciality.speciality')),
            ],
        ),
    ]
