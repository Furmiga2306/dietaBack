# Generated by Django 5.1.6 on 2025-02-14 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='John Doe', max_length=255),
            preserve_default=False,
        ),
    ]
