from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .controller import SimpleQuery
from .models import Customers, Drivers, Schedule
from .serializers import (
    CustomererSerializers,
    DriverSerializers,
    FilterDriversSerializers,
    NameFilterDriversSerializers,
    ScheduleSerializers,
)


# Class Create drivers
class DriversViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializers
    lookup_field = "name"

    def get_queryset(self):
        queryset = Drivers.objects.filter(status=True)
        return queryset

    # Create drivers
    def post(self, request):

        driver_Serializers = DriverSerializers(data=request.data)
        if driver_Serializers.is_valid():
            driver_Serializers.save()
            return Response(driver_Serializers.data)
        return Response(driver_Serializers.errors)


# Class of customers
class CustomViewSet(viewsets.ModelViewSet):
    serializer_class = CustomererSerializers
    lookup_field = "name"

    # list customers
    def get_queryset(self):
        queryset = Customers.objects.filter(status=True)
        return queryset

    # Create customs
    def post(self, request):
        customer_Serializers = CustomererSerializers(data=request.data)
        if customer_Serializers.is_valid():
            customer_Serializers.save()
            return Response(customer_Serializers.data)
        return Response(customer_Serializers.errors)


# class of schedule
class AllScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializers
    lookup_field = "date"

    # list schedule
    def get_queryset(self):
        queryset = Schedule.objects.filter(status=True)
        return queryset


class SaveScheduleView(APIView):
    # Create schedule
    def post(self, request):

        schedule_Serializers = ScheduleSerializers(data=request.data)
        if schedule_Serializers.is_valid():
            if SimpleQuery.ValidateSheduleDriver(Schedule, schedule_Serializers):
                print()
                schedule_Serializers.save()
                return Response(schedule_Serializers.data)
            else:
                return Response({"messague": "the space is occupied"})

        return Response(schedule_Serializers.errors)


# Class filter by date sort by time
class TimeScheduleView(APIView):

    # list schedule per date and time
    def get(self, request, date="2022-09-01"):
        print(SimpleQuery.OrderByDate_time(Schedule, date))
        return Response(FilterDriversSerializers(SimpleQuery.OrderByDate_time(Schedule, date), many=True).data)


# Class filter by driver, date order by time
class FilterDriversView(APIView):

    # list schedule per date and time
    def get(self, request, id=0, date="2022-09-01"):
        return Response(FilterDriversSerializers(SimpleQuery.FilterDriverTime(Schedule, id, date), many=True).data)


# Class search driver by time and location
class SearchDriversView(APIView):

    # list schedule per date and time
    def get(self, request, time="10:00:00", date="2022-09-01", lat=0, lng=0):
        data = FilterDriversSerializers(SimpleQuery.SearchDriverTime(Schedule, time, date), many=True).data
        time = SimpleQuery.ValTime(time)
        valdata = NameFilterDriversSerializers(SimpleQuery.SearchDriverTime(Schedule, time, date), many=True).data
        data = SimpleQuery.ValidateDrivers(data, valdata)
        search = SimpleQuery.SearchDriver(lat, lng, data)
        return Response(search)
