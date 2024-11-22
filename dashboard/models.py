from django.db import models

# Create your models here.
class Users(models.Model):
    class Meta:
        db_table = "users"
    
    name = models.CharField(max_length=50, null=True, default=None, blank=True)
    email = models.CharField(max_length=50, null=True, default=None, db_collation="utf8mb4_0900_ai_ci", blank=True)
    email_verified_at = models.DateTimeField(null=True, default=None)
    password = models.CharField(max_length=100, null=True, default=None, blank=True)
    gender = models.CharField(max_length=10, null=True, default=None, blank=True)
    dob = models.DateTimeField(null=True, default=None)
    avatar_id = models.BigIntegerField(null=True, default=None)
    image_data = models.TextField(null=True, default=None, blank=True)
    first_signup_mail = models.BooleanField(default=1)
    is_active = models.BooleanField(null=True, default=None)
    is_deleted = models.BooleanField(null=True, default=None)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)