# Generated by Django 3.2.3 on 2021-07-04 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210703_1144'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.RemoveField(
            model_name='usertherapyactivity',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='usertherapysession',
            name='therapy_list',
        ),
        migrations.DeleteModel(
            name='PackProgram',
        ),
    ]
