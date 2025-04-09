# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Show(models.Model):

    #__Show_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    travel = models.TextField(max_length=255, null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)
    bandhotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    crewhotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    #__Show_FIELDS__END

    class Meta:
        verbose_name        = _("Show")
        verbose_name_plural = _("Show")


class Venue(models.Model):

    #__Venue_FIELDS__
    address = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    showers = models.BooleanField()
    laundry = models.BooleanField()
    greenroom = models.TextField(max_length=255, null=True, blank=True)
    wifinetwork = models.TextField(max_length=255, null=True, blank=True)
    wifipassword = models.TextField(max_length=255, null=True, blank=True)

    #__Venue_FIELDS__END

    class Meta:
        verbose_name        = _("Venue")
        verbose_name_plural = _("Venue")


class Venuecontacts(models.Model):

    #__Venuecontacts_FIELDS__
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    dayofshow = models.TextField(max_length=255, null=True, blank=True)
    production = models.TextField(max_length=255, null=True, blank=True)
    ld = models.TextField(max_length=255, null=True, blank=True)
    merch = models.TextField(max_length=255, null=True, blank=True)
    hospitality = models.TextField(max_length=255, null=True, blank=True)
    settlement = models.TextField(max_length=255, null=True, blank=True)
    buyer = models.TextField(max_length=255, null=True, blank=True)

    #__Venuecontacts_FIELDS__END

    class Meta:
        verbose_name        = _("Venuecontacts")
        verbose_name_plural = _("Venuecontacts")


class Guestlist(models.Model):

    #__Guestlist_FIELDS__
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    #__Guestlist_FIELDS__END

    class Meta:
        verbose_name        = _("Guestlist")
        verbose_name_plural = _("Guestlist")


class Guestlistentry(models.Model):

    #__Guestlistentry_FIELDS__
    guestlist = models.ForeignKey(GuestList, on_delete=models.CASCADE)
    name = models.TextField(max_length=255, null=True, blank=True)
    numtickets = models.IntegerField(null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)

    #__Guestlistentry_FIELDS__END

    class Meta:
        verbose_name        = _("Guestlistentry")
        verbose_name_plural = _("Guestlistentry")


class Hotel(models.Model):

    #__Hotel_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)

    #__Hotel_FIELDS__END

    class Meta:
        verbose_name        = _("Hotel")
        verbose_name_plural = _("Hotel")



#__MODELS__END
