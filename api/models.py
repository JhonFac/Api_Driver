from django.db import models


class Drivers(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Customers(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    driver = models.ForeignKey(Drivers, null=False, blank=True, on_delete=models.CASCADE, default=0)
    custom = models.ForeignKey(Customers, null=False, blank=True, on_delete=models.CASCADE, default=0)
    time = models.TimeField(auto_now=False, auto_now_add=False, default="00:00:00")
    date = models.DateField(auto_now=False, auto_now_add=False, default="2022-09-20")
    rec_lat = models.IntegerField()
    rec_lng = models.IntegerField()
    des_lat = models.IntegerField()
    des_lng = models.IntegerField()
    status = models.BooleanField(default=True)
