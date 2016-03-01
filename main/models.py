# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Concert(models.Model):
    place = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_time = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    content = models.TextField()

class Comment(models.Model):
    nickname = models.CharField(max_length=60)
    published_date = models.DateTimeField(
            blank=True, null=True)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nickname

    def approve(self):
        self.approved_comment = True
        self.save()