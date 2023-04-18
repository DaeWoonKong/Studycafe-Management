from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils import timezone

class Seat(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    modify_date = models.DateTimeField(null=True, blank=True)
    scode = models.CharField(max_length=10)
    scondition = models.TextField(default='사용가능')
    unitprice = models.IntegerField(default=0)
    discountrate = models.DecimalField(max_digits=11, decimal_places=2,default=0)
    imgfile = models.ImageField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.scode+" " +self.scondition+" " +str(self.unitprice)+" " +str(self.discountrate)