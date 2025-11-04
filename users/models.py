from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    membership_id = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, default='Active')
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    index = models.IntegerField(default=0)

    class Meta:
        db_table = 'users_user'
    def __str__(self):
        return self.name





