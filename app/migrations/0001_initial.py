# Generated by Django 4.1.3 on 2022-12-01 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCall',
            fields=[
                ('datetime', models.DateTimeField(verbose_name='date and time')),
                ('phone_number', models.CharField(max_length=14)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('RECEIVE', 'Incoming call'), ('SEND', 'Outgoing call'), ('MISS', 'Missed call')], max_length=13)),
                ('duration', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'calls',
            },
        ),
        migrations.CreateModel(
            name='TextMessage',
            fields=[
                ('datetime', models.DateTimeField(verbose_name='date and time')),
                ('phone_number', models.CharField(max_length=14)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('RECEIVE', 'Received text'), ('SEND', 'Sent text')], max_length=13)),
            ],
            options={
                'db_table': 'messages',
            },
        ),
    ]
