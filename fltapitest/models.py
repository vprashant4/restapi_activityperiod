from django.db import models
from timezone_field import TimeZoneField


class User(models.Model):
   id = models.CharField(primary_key=True, max_length=20)
   real_name = models.CharField(max_length=50)
   tz = TimeZoneField(default='Europe/London')

   def __str__(self):
      return self.real_name


class ActivityPeriod(models.Model):
   user = models.ForeignKey(User, related_name='activity_periods', on_delete=models.CASCADE)
   start_time = models.DateTimeField()
   end_time = models.DateTimeField()

   def __str__(self):
      return str(self.user)
