from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 20, unique=True, null=True, default=None)
    email = models.CharField(max_length=320)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.username