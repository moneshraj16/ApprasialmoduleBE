# Generated by Django 3.0.4 on 2022-05-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeservice', '0006_auto_20220525_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='code',
            field=models.CharField(max_length=24, null=True, unique=True),
        ),
    ]
