# Generated by Django 5.0.7 on 2024-09-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='tickets_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]