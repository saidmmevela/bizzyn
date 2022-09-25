from django.db import models
from django.utils import timezone

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_live = models.BooleanField()
    amount = models.FloatField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%H: %M: %S')}"
    
    class Meta:
        ordering = ("created_at",)

class UserModel(models.Model):
    REQUIRED_FIELDS = ('full_name','token','password')
    USERNAME_FIELD = ('username')
    is_anonymous = ('token')
    is_authenticated = ('token')
    full_name = models.CharField(max_length=255, unique=True,null=False,blank=False)
    username = models.CharField(max_length=255, unique=True)
    token = models.CharField(max_length=255,null=False)
    password = models.CharField(max_length=255, null=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.full_name} - {self.created_at.strftime('%H: %M: %S')}"
    
    class Meta:
        ordering = ("created_at",)
    
class Modelx(models.Model):
    test_content = models.OneToOneField(
        TestModel, on_delete = models.CASCADE, related_name="test_content"
    )
    mileage = models.FloatField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.test_content.name} - {self.mileage}"
