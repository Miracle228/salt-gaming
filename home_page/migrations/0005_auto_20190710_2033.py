# Generated by Django 2.2.2 on 2019-07-10 14:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='posted_time',
        ),
        migrations.AddField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=200),
        ),
    ]