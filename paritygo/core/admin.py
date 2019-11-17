from django.contrib import admin
from core.models import House, HouseRoom, RoomLight, Sensor, RoomSensor, ThermostatMode
from core.models import HouseThermostat, Light, Thermostat, RoomLightStateAudit

admin.site.register(House)
admin.site.register(HouseRoom)
admin.site.register(Light)
admin.site.register(RoomLight)
admin.site.register(RoomLightStateAudit)
admin.site.register(Sensor)
admin.site.register(RoomSensor)
admin.site.register(Thermostat)
admin.site.register(ThermostatMode)
admin.site.register(HouseThermostat)
