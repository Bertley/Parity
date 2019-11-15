import uuid

from django.db import models
from django.contrib.auth import get_user_model


class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    issued_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Customer {0}".format(str(self.id))


class HouseRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    house = models.ForeignKey(
        'House',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "Customer {0} Room".format(str(self.house))


class Light(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class RoomLight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    light_id = models.ForeignKey(
        'Light',
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        'HouseRoom',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "Light in Room {0}".format(str(self.room))


class Sensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class RoomSensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(
        'HouseRoom',
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        'Sensor',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0} Sensor in Room {1}".format(str(self.sensor), str(self.room))


class Thermostat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class ThermostatMode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class HouseThermostat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thermostat = models.ForeignKey(
        'Thermostat',
        on_delete=models.CASCADE
    )
    house = models.ForeignKey(
        'House',
        on_delete=models.CASCADE
    )
    mode = models.ForeignKey(
        'ThermostatMode',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0} Mode at House {1}".format(str(self.mode), str(self.house))
