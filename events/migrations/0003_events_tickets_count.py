# Generated by Django 5.0.7 on 2024-09-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_events_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='tickets_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
