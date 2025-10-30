from django.db import models

# Create your models here.

class Day(models.Model):
    days = [(x,x) for x in (range(1,25))]
    day = models.SmallIntegerField(blank=False,choices=days,unique=True)
    is_unlocked = models.BooleanField(blank=False)
    award_quote = models.CharField(blank=True)
    award_image = models.CharField(blank=True)
    award_link = models.URLField(max_length=255,blank=True)
    text = models.CharField(blank=False)
    def __str__(self):
        return str(self.day)