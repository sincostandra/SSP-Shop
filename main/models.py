from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here..
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=36)
    price = models.IntegerField()
    pack_category = models.CharField(max_length=36)
    level_category = models.CharField(max_length=36)
    description = models.TextField()

    @property
    def is_pro_category(self):
        return True if self.level_category == 'Pro' else False
