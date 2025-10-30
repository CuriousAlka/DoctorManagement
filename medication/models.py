from django.db import models

from users.models import User


# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    dosage = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name