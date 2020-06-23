from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from .helper import random_pk, TIMEZONES


class User(models.Model):
	user_id = models.CharField(max_length=9, primary_key=True, unique=True, blank=True, editable=False, default=random_pk)
	real_name = models.CharField(max_length=32, blank=True)
	tz = models.CharField(max_length=32, choices=TIMEZONES)


	def __str__(self):
		return self.real_name



class Activity(models.Model):
	user = models.ForeignKey(User, related_name='activities', on_delete=models.CASCADE)
	start_time = models.DateTimeField(null=True, default=None)
	end_time = models.DateTimeField(null=True, default=None)

	def clean(self):
		if self.start_time > self.end_time:
			raise ValidationError("Dates are invalid! End time can't be before start time")
