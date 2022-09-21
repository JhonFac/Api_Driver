from numbers import Integral

from rest_framework import serializers

from .models import Customers, Drivers, Schedule


class DriverSerializers(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = "__all__"


class CustomererSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"


class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class FilterDriversSerializers(serializers.ModelSerializer):
    driver = serializers.StringRelatedField()
    custom = serializers.StringRelatedField()

    class Meta:
        model = Schedule
        fields = "__all__"


class NameFilterDriversSerializers(serializers.ModelSerializer):
    driver = serializers.StringRelatedField()

    class Meta:
        model = Schedule
        fields = ["driver"]
