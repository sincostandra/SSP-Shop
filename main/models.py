from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=36)
    price = models.IntegerField()
    pack_category = models.CharField(max_length=36)
    level_category = models.CharField(max_length=36)
    description = models.TextField()

    @property
    def is_pro_category(self):
        return True if self.level_category == 'Pro' else False
