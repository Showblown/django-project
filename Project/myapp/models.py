from django.db import models

class User(models.Model):
    # any data from the user that we would like to have
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    gender = models.CharField(max_length = 10)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

# A table User will get created in the database and it will look like:

# Name      Age     Gender      Email       Password
# abc       17        F         ab@h.com    231#
# vgf       27        M         ty@h.com    121#
# tyu       57        F         6b@h.com    251#

# Create your models here.
