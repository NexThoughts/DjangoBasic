from django.db import models



class University(models.Model):
    name=models.CharField(max_length=70,null=False)

class College(models.Model):
    name=models.CharField(max_length=70,null=False)
    university=models.ForeignKey(University)
    area=models.CharField(max_length=70)