# Generated by Django 5.0.4 on 2024-04-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_rename_emp_id_emp_eid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='emp',
            name='department',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='emp',
            name='eid',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='emp',
            name='is_working',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='emp',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
