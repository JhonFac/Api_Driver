from .serializers import ScheduleSerializers


class SimpleQuery:

    #  Filtrar for daate and order by time
    def OrderByDate_time(o, date):

        if date != 0:
            return o.objects.filter(date=date, status=True).order_by("time")
        else:
            return o.objects.filter(status=True).order_by("time")

    #  check if the space is free on schedule
    def ValidateSheduleDriver(s, Sdata):
        time = Sdata.validated_data.get("time")
        date = Sdata.validated_data.get("date")
        driver = Sdata.validated_data.get("driver")
        data = s.objects.filter(time=time, date=date, driver=driver, status=True).order_by("time")
        data = ScheduleSerializers(data, many=True).data

        if len(data) > 0:
            return False
        else:
            return True

    # quiery for driver id and schedule date
    def FilterDriverTime(s, id, date):
        return s.objects.filter(driver=id, date=date, status=True).order_by("time")

    # filter schedule for time and date
    def SearchDriverTime(s, time, date):
        return s.objects.filter(time=time, date=date, status=True).order_by("time")

    # validate data looking for the closest driver
    def SearchDriver(lat, lng, data):
        closest = 200
        for i in range(len(data)):
            minlat = data[i]["des_lat"] - lat
            minlng = data[i]["des_lng"] - lng
            if minlat < 0:
                minlat = minlat * (-1)
            if minlng < 0:
                minlng = minlng * (-1)

            if closest > (minlat + minlng):
                driver = i
                endlat = minlat
                endlng = minlng
                closest = minlat + minlng

        return {"name": data[driver]["driver"], "lat": endlat, "lng": endlng}

    # add an hour to validate if you have free space
    def ValTime(t):
        return str(int(t.split(":")[0]) + 1) + ":00:00"

    # remove the conductors that do not have the free schedule
    def ValidateDrivers(data, valdata):
        for name in range(len(valdata)):
            for i in data:
                if i["driver"] == valdata[name]["driver"]:
                    data.pop(data.index(i))
        return data
