from statistics import mode
from django.db import models
from accounts.models import Account
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=50)
    short=models.CharField(max_length=50)
    description=models.TextField()
    is_active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    def __unicode__(self):
        return self.product