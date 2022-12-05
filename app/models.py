from django.db import models
from django.utils import timezone

# Create your models here.

# Abstract base class to combine with other models
# DOES NOT HAVE DB TABLE


class CommonInfo(models.Model):
    datetime = models.DateTimeField('date and time')
    phone_number = models.CharField(max_length=14)

    class Meta:
        abstract = True

    def __str__(self):
        # maybe I should concat the id/date to differentiate calls/texts?
        return self.phone_number


class PhoneCall(CommonInfo):
    id = models.BigAutoField(primary_key=True)
    CALL_TYPES = [
        ('RECEIVE', 'Incoming call'),
        ('SEND', 'Outgoing call'),
        ('MISS', 'Missed call'),
    ]
    type = models.CharField(choices=CALL_TYPES, max_length=13)
    duration = models.PositiveIntegerField()  # range is 0 to 2147483647

    class Meta:
        db_table = 'calls'


class TextMessage(CommonInfo):
    id = models.BigAutoField(primary_key=True)
    MESSAGE_TYPES = [
        ('RECEIVE', 'Received text'),
        ('SEND', 'Sent text'),
    ]
    type = models.CharField(choices=MESSAGE_TYPES, max_length=13)

    class Meta:
        db_table = 'messages'
