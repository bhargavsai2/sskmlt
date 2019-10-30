# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class Profile(AbstractBaseUser):

    username = models.CharField(max_length = 100, unique = True)
    first_name = models.CharField(max_length = 30, blank = True)
    last_name = models.CharField(max_length = 30, blank = True)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    is_superuser = models.BooleanField(default = False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

class Lorry(models.Model):
    truck_no = models.CharField(max_length=50,help_text='truck No')
    driver_name = models.CharField(max_length=30,help_text='Driver name')
    driver_id = models.CharField(max_length=50,help_text="Driver ID",null=True,blank=True)
    driver_contact = models.CharField(max_length=50,help_text="Contact")
    owner_name = models.CharField(max_length=50,help_text="Owner name")
    owner_contact = models.CharField(max_length=50,help_text="Owner Contact")
    licence_id = models.CharField(max_length=40,help_text="licence_id")
    commission_amount = models.FloatField(null=True,blank=True)

class CustomerCosignee(models.Model):
    customer_name = models.CharField(max_length=40,help_text='Customer name')
    contact = models.CharField(max_length=40,help_text='Contact')
    address = models.CharField(max_length=100,help_text='address')

class CustomerConsigner(models.Model):
    customer_name = models.CharField(max_length=40,help_text='Customer name')
    contact = models.CharField(max_length=40,help_text="contact")
    address = models.CharField(max_length=100,help_text="address")
    
class AccountEntry(models.Model):
    customer_consignee = models.ForeignKey(CustomerCosignee)
    customer_consigner = models.ForeignKey(CustomerConsigner)
    truck = models.ForeignKey(Lorry)
    date = models.DateField()
    tons = models.FloatField(null=True,blank=True,default='0.0')
    freight = models.FloatField(null=True,blank=True,default='0.0')
    advance = models.FloatField(null=True,blank=True,default='0.0')
    balance = models.FloatField(null=True,blank=True,default='0.0')
    hamali = models.FloatField(null=True,blank=True,default='0.0')
    netcollection = models.FloatField(null=True,blank=True,default='0.0')
    collection_date = models.DateField(null=True,blank=True)
    paid_date = models.DateField(null=True,blank=True)
    paid_balance = models.FloatField(null=True,blank=True,default='0.0')
    station = models.CharField(max_length=10,null=True,blank=True)
    driver_paid_balance = models.FloatField()