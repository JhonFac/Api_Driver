# Generated by Django 4.1.1 on 2022-09-21 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_schedule_custom_alter_schedule_driver"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedule",
            name="date",
            field=models.DateField(default="2022-09-20"),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="time",
            field=models.TimeField(default="00:00:00"),
        ),
    ]
