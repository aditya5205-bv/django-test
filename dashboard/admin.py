from django.contrib import admin
# from django.contrib.auth.base_user import AbstractBaseUser 

from django import forms
from django.forms.widgets import RadioSelect

# Register your models here.
from .models import Users

@admin.action(description="Mark as active")
def mark_active(modeladmin, request, queryset):
    queryset.update(is_active = 1)

@admin.action(description="Mark as deleted")
def mark_deleted(modeladmin, request, queryset):
    queryset.update(is_deleted = 1)
    
    

    
    
class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            # 'email_verified_at': forms.DateTimeInput(attrs={'type': 'date'}),
            # 'first_signup_mail': forms.BooleanField()
        }

class UsersAdmin(admin.ModelAdmin):
    form = UsersForm
    
    search_fields = ("name",)
    
    list_filter = ("is_active", "is_deleted")
    
    cols = [
        "id",
        "name",
        "email",
        "password",
        "email_verified_at",
        "dob",
        "gender",
        "image_data",
        "first_signup_mail",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at"
    ]

    def get_readonly_fields(self, request, obj=None):
        # readonly_fields = list(super(UsersAdmin, self).get_readonly_fields(request, obj))
        # createonly_fields = list(getattr(self, 'createonly_fields', []))
            
        if obj: return ["password"]
        else: return []
    
    
    actions = [mark_active, mark_deleted]
    
    list_display = [
        "id",
        "name",
        "email",
        "email_verified_at",
        "dob",
        "image_data",
        "first_signup_mail",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at"
    ]
    
    # exclude=["gender", "password"]
    
    fieldsets = [
        (
            None,
            {
                "fields": [
                        "name",
                        "email",
                        "password",
                        "dob", 
                        "email_verified_at",
                        "gender",
                        "image_data",
                        "first_signup_mail",
                        "is_active",
                        "is_deleted",
                    ]
            }
        )
    ]
    
    # list_editable = 
    # [
    #     "name",
    #     "email",
    #     "email_verified_at",
    #     "dob",
    #     "image_data",
    #     "first_signup_mail",
    #     "is_active",
    #     "is_deleted",
    #     "created_at",
    #     "updated_at"
    # ]
    
    # fields = [
    #     "name",
    #     "email",
    #     "password",
    #     "email_verified_at",
    #     "dob",
    #     "image_data",
    #     "first_signup_mail",
    #     "is_active",
    #     "is_deleted",
    #     # "created_at",
    #     # "updated_at"
    # ]
    
    readonly_fields = ["password", "created_at", "updated_at"]
    

admin.site.register(Users, UsersAdmin)