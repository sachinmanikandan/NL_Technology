from django.db import models
from django.contrib.auth.models import User



class Shift(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


class Man(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    shift = models.ForeignKey('Shift', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name or "Unnamed"



class Machine(models.Model):
    name = models.CharField(max_length=100)
    machine_id = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)
    material_id = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Method(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    responsible_man = models.ForeignKey(Man, on_delete=models.SET_NULL, null=True)
    machines = models.ManyToManyField(Machine, blank=True)
    materials = models.ManyToManyField(Material, blank=True)

    def __str__(self):
        return self.name

class MachineUsage(models.Model):
    man = models.ForeignKey(Man, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.man} - {self.machine}"
