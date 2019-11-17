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
    field_history = FieldHistoryTracker(['value'])

    def __str__(self):
        return "Room sensor {0}".format(str(self.id))

class HouseThermostat(models.Model):
      # Declare status
    MODE_OFF = 0
    MODE_COOL = 1
    MODE_HEAT = 2
    MODE_FAN_ON = 3
    MODE_AUTO = 4
    MODE_CHOICES = (
        (MODE_OFF, 'off'),
        (MODE_COOL, 'cool'),
        (MODE_HEAT, 'heat'),
        (MODE_FAN_ON, 'fan-on'),
        (MODE_AUTO, 'auto')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    house = models.ForeignKey('House', on_delete=models.CASCADE)
    mode = FSMIntegerField(choices=MODE_CHOICES, default=MODE_OFF)

    field_history = FieldHistoryTracker(['mode'])

    def __str__(self):
        return "{0}".format(str(self.id))

