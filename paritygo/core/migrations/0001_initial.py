# Generated by Django 2.2.7 on 2019-11-17 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_fsm
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('issued_date', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HouseRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.House')),
            ],
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
                ('unit', models.CharField(default='Celcius', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RoomSensor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.FloatField(default=0)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.HouseRoom')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Sensor')),
            ],
        ),
        migrations.CreateModel(
            name='RoomLight',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'off'), (1, 'on')], default=0)),
                ('light', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Light')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.HouseRoom')),
            ],
        ),
        migrations.CreateModel(
            name='HouseThermostat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mode', django_fsm.FSMIntegerField(choices=[(0, 'off'), (1, 'cool'), (2, 'heat'), (3, 'fan-on'), (4, 'auto')], default=0)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.House')),
            ],
        ),
    ]
