from django.db import models

# Create your models here.

class Day(models.Model):
    days = [(x,x) for x in (range(1,25))]
    day = models.SmallIntegerField(blank=False,choices=days,unique=True)
    open_date = models.DateTimeField(blank=True,null=True)
    award_quote = models.CharField(blank=True)
    award_image = models.CharField(blank=True)
    award_link = models.URLField(max_length=255,blank=True)
    text = models.CharField(blank=False)
    def __str__(self):
        return str(self.day)