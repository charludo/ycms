# Generated by Django 4.2.3 on 2023-11-19 08:32

from django.db import migrations, models

import ycms.cms.models.timetravel_manager


class Migration(migrations.Migration):
    """
    Use the a custom function instead of timezone.now() whenever we are time-travelling
    """

    dependencies = [("cms", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="bed",
            name="created_at",
            field=models.DateTimeField(
                default=ycms.cms.models.timetravel_manager.current_or_travelled_time
            ),
        ),
        migrations.AlterField(
            model_name="bedassignment",
            name="created_at",
            field=models.DateTimeField(
                default=ycms.cms.models.timetravel_manager.current_or_travelled_time
            ),
        ),
        migrations.AlterField(
            model_name="medicalrecord",
            name="created_at",
            field=models.DateTimeField(
                default=ycms.cms.models.timetravel_manager.current_or_travelled_time
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="created_at",
            field=models.DateTimeField(
                default=ycms.cms.models.timetravel_manager.current_or_travelled_time
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="created_at",
            field=models.DateTimeField(
                default=ycms.cms.models.timetravel_manager.current_or_travelled_time
            ),
        ),
        migrations.AlterField(
            model_name="ward",
            name="created_at",
            field=models.DateTimeField(
                default=ycms.cms.models.timetravel_manager.current_or_travelled_time
            ),
        ),
    ]
