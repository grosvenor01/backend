# Generated by Django 4.1.5 on 2023-01-27 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_pub_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pub',
            name='type',
            field=models.CharField(choices=[('theme', 'theme'), ('question', 'question')], max_length=10),
        ),
    ]