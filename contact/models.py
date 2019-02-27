# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class contact(models.Model):
    Email = models.CharField(max_length=20)
    Twiiter = models.CharField(max_length=20)
    Github = models.CharField(max_length=20)
    


    def __unicode__(self):
        return self.Email
