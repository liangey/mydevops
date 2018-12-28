from django.db import models

# Create your models here.
'''
models.CharField
models.IntegerField
models.FloatField
models.AutoField
models.TextField
models.EmailField
models.DateField
models.DateTimeField
models.ImageField
models.URLField
models.IPAddressField
'''

class userinfo(models.Model):
    nid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=32)
    email=models.EmailField()
    memo=models.TextField()





