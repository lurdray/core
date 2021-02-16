from django.db import models
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
    threshold = models.IntegerField(default=1)
    location = models.CharField(max_length=30, blank=True)
    size = models.CharField(max_length=20, blank=True)
    #description = models.TextField(default=None)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name