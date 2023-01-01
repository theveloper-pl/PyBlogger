from statistics import mode
from django.db import models

# Create your models here.

# class Post(models.Model):
#     user=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     cart=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
#     variations=models.ManyToManyField(Variation,blank=True)
#     quantity=models.IntegerField()
#     is_active=models.BooleanField(default=True)

#     def sub_total(self):
#         return self.product.price * self.quantity
        
#     def __unicode__(self):
#         return self.product