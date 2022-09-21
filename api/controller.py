from .serializers import ScheduleSerializers


class SimpleQuery:
    def OrderByDate_time(o, date):

        if date != 0:
            return o.objects.filter(date=date, status=True).order_by("time")
        else:
            return o.objects.filter(status=True).order_by("time")

    def ValidateSheduleDriver(s, data):
        data = s.objects.filter(time=data["time"], date=data["date"], driver=data["driver"], status=True).order_by(
            "time"
        )
        data = ScheduleSerializers(data, many=True).data
        print(data)
        if len(data) > 0:
            return False
        else:
            return True

    def FilterDriverTime(s, id, date):
        return s.objects.filter(driver=id, date=date, status=True).order_by("time")

    def SearchDriverTime(s, time, date):
        return s.objects.filter(time=time, date=date, status=True).order_by("time")

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

    def ValTime(t):
        return str(int(t.split(":")[0]) + 1) + ":00:00"

    def ValidateDrivers(data, valdata):
        for name in range(len(valdata)):
            for i in data:
                if i["driver"] == valdata[name]["driver"]:
                    data.pop(data.index(i))
        return data
