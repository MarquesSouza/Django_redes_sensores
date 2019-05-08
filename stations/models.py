from django.db import models
class Metric(models.Model):
    name = models.CharField(max_length=30)
    unit = models.CharField(max_length=20)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name
class Device(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    status = models.BooleanField()
    def __str__(self):
        return self.name
class Contributor(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    site = models.EmailField(max_length=50)
    logo = models.CharField(max_length=50,null=True)
    telefone = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Station(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    status = models.BooleanField()
    location = models.TextField(max_length=300)
    latitude = models.DecimalField(max_digits=19,decimal_places=10)
    longitude = models.DecimalField(max_digits=19,decimal_places=10)
    contributors_id = models.OneToOneField(Contributor,on_delete=models.CASCADE,null = True, blank=True)
    def __str__(self):
        return self.name
class Measure(models.Model):
    date = models.DateTimeField()
    measure = models.FloatField(max_length=100)
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    metric_id = models.ForeignKey(Metric, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.date) + "/" + str(self.station_id)+"/"+str(self.device_id)
