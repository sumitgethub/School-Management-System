from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from School.models import School
from Master.models import Gender

class SchoolUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    phone_number = models.CharField(max_length=50,unique=True,blank=True,null=True)
    unique_id = models.CharField(max_length=12,unique=True,blank=True,null=True)
    email = models.EmailField(max_length=30,unique=True)
    school = models.OneToOneField(School, on_delete=models.CASCADE,null=True, blank=True)
    username = None
    created_time_stamp = models.DateTimeField(auto_now_add=True)
    update_by_time_stamp = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)

    objects = SchoolUserManager()
    USERNAME_FIELD = "unique_id"
    REQUIRED_FIELD = []

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,unique=True)
    photo = models.ImageField(upload_to="ProfileImg",blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    gender = models.ForeignKey(Gender,on_delete=models.SET_NULL,null=True, blank=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    address2 =models.CharField(max_length=200,blank=True,null=True)
    landmark = models.CharField(max_length=200,blank=True,null=True)
    pincode = models.CharField(blank=True,null=True,max_length = 10)
    city = models.CharField(max_length=100,blank=True,null=True)
    district = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)
    
    def __str__(self):
        return self.user.unique_id



