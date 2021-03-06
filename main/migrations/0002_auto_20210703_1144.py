# Generated by Django 3.2.3 on 2021-07-03 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recurrence.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PackProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserTherapyActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField(default=None, verbose_name='reps')),
                ('complete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserTherapySession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recurrences', recurrence.fields.RecurrenceField()),
                ('therapy_list', models.ManyToManyField(through='main.PackProgram', to='main.UserTherapyActivity')),
            ],
        ),
        migrations.RemoveField(
            model_name='therapyactivity',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='therapyactivity',
            name='text',
        ),
        migrations.RemoveField(
            model_name='therapyactivity',
            name='therapylist',
        ),
        migrations.AddField(
            model_name='therapyactivity',
            name='description',
            field=models.TextField(default=None, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='therapyactivity',
            name='name',
            field=models.CharField(default=None, max_length=300, verbose_name='Activity Name'),
        ),
        migrations.DeleteModel(
            name='TherapyList',
        ),
        migrations.AddField(
            model_name='usertherapyactivity',
            name='therapy_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.therapyactivity'),
        ),
        migrations.AddField(
            model_name='usertherapyactivity',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='packprogram',
            name='user_therapy_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usertherapyactivity'),
        ),
        migrations.AddField(
            model_name='packprogram',
            name='user_therapy_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usertherapysession'),
        ),
    ]
