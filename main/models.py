from django.db import models
from django.contrib.auth.models import User

class Equipment(models.Model):
    eq_id = models.IntegerField()
    eq_name = models.CharField(max_length=200)
    amount = models.IntegerField()

    def __str__(self):
        return self.eq_name


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    reservation_id = models.IntegerField()
    date = models.DateField()
    hour = models.TimeField()
    track = models.IntegerField(null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)

    def __str__(self):
        if self.equipment == None:
             return str(self.date) + ' ' + self.user.username +  " Track: " +str(self.track)
        else:
            return str(self.date) + ' ' + self.user.username + " Eq: " + str(self.equipment.eq_name)

class AvailableReservationsTrack(models.Model):
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    track1 = models.BooleanField(default=False)
    track2 = models.BooleanField(default=False)
    track3 = models.BooleanField(default=False)
    track4 = models.BooleanField(default=False)
    track5 = models.BooleanField(default=False)
    track6 = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.date) + ' '+ str(self.time_from) + ' '+ str(self.time_to)


class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work', null=True, blank=True)
    time = models.DateTimeField()
    is_working = models.BooleanField()

    def __str__(self):
        return str(self.user.username) + ' '+ str(self.time) + ' is working:'+ str(self.is_working)
    

