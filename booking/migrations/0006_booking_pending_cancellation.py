# Generated by Django 5.0.7 on 2024-09-02 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_rename_event_booking_name_remove_booking_event_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='pending_cancellation',
            field=models.BooleanField(default=False),
        ),
    ]
