# Generated by Django 3.2.3 on 2021-07-04 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210704_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertherapysession',
            name='therapy_list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.usertherapyactivity'),
        ),
        migrations.AlterField(
            model_name='usertherapyactivity',
            name='therapy_activity',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.therapyactivity'),
        ),
    ]
