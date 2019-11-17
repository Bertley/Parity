import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django_fsm import FSMIntegerField
from field_history.tracker import FieldHistoryTracker


class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    issued_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}".format(str(self.address))


class HouseRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    house = models.ForeignKey('House', on_delete=models.CASCADE)

    def __str__(self):
        return "{0}'s Room {1}".format(str(self.house), str(self.id))


class Light(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class RoomLight(models.Model):
    # Declare status
    STATUS_OFF = 0
    STATUS_ON = 1
    STATUS_CHOICES = (
        (STATUS_OFF, 'off'),
        (STATUS_ON, 'on')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    light = models.ForeignKey('Light', on_delete=models.CASCADE)
    room = models.ForeignKey('HouseRoom', on_delete=models.CASCADE)
    status = FSMIntegerField(choices=STATUS_CHOICES, default=STATUS_OFF)

    field_history = FieldHistoryTracker(['status'])

    def __str__(self):
        return "Room light {0}".format(str(self.id))


class Sensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=255)
    unit = models.CharField(max_length=255, null=False,
                            blank=False, default="Celcius")

    def __str__(self):
        return self.label


class RoomSensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey('HouseRoom', on_delete=models.CASCADE)
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    value = models.FloatField(null=False, blank=False, default=0)
    field_history = FieldHistoryTracker(['value', 'sensor'])

    def __str__(self):
        return "Room sensor {0}".format(str(self.id))


class Thermostat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class ThermostatMode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class HouseThermostat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thermostat = models.ForeignKey('Thermostat', on_delete=models.CASCADE)
    house = models.ForeignKey('House', on_delete=models.CASCADE)
    mode = models.ForeignKey('ThermostatMode', on_delete=models.CASCADE)

    field_history = FieldHistoryTracker(['mode'])

    def __str__(self):
        return self.id
