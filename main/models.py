from django.db import models
import uuid


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    image = models.TextField(blank=True)

    @property
    def is_available(self):
        return self.quantity > 0
