from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
import datetime
from django.utils import timezone
from django.conf import settings


class AccountManager(BaseUserManager):
    def create_user(self, Email, Password=None, **kwargs):
        # Ensure that an email address is set
        if not Email:
            raise ValueError('Users must have a valid e-mail address')


        account = self.model(
            Email=self.normalize_email(Email),
            FirstName=kwargs.get('FirstName', None),
            LastName=kwargs.get('LastName', None),
            PhoneNumber= kwargs.get('PhoneNumber', None),
            Gender=kwargs.get('Gender', None),
            Image=kwargs.get('Image', None),
        )
        account.set_password(Password)
        account.save()

        return account


class Account(AbstractBaseUser):
    UserId=models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100, blank=True)
    LastName = models.CharField(max_length=100, blank=True)
    Email = models.EmailField(unique=True)
    PhoneNumber = models.CharField(max_length=100, blank=True)
    Gender = models.CharField(max_length=10)
    Image= models.CharField(max_length=60000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['FirstName']




class Feeds(models.Model):
    FeedId=models.AutoField(primary_key=True)
    FeedImage = models.CharField(max_length=60000)
    Description = models.CharField(max_length=200)
    UserId = models.ForeignKey(Account, related_name='post_by', on_delete=models.CASCADE)
    FeedTime = models.CharField(max_length=200)
    @property
    def FirstName(self):
        return self.UserId.FirstName
    @property
    def Image(self):
        return self.UserId.Image
    @property
    def Id(self):
        return self.FeedId




class Likes(models.Model):
    LikeId=models.AutoField(primary_key=True)
    FeedId =  models.ForeignKey(Feeds, related_name='like_on', on_delete=models.CASCADE)
    UserId = models.ForeignKey(Account, related_name='like_by', on_delete=models.CASCADE)
    LikeTime = models.CharField(max_length=200)


    @property
    def LikeCount(self):
        return Likes.objects.filter(FeedId=self.FeedId).count()




class Comments(models.Model):
    CommentId=models.AutoField(primary_key=True)
    FeedId =  models.ForeignKey(Feeds, related_name='Comments_on', on_delete=models.CASCADE)
    UserId = models.ForeignKey(Account, related_name='Comments_by', on_delete=models.CASCADE)
    Comment = models.CharField(max_length=200)
    CommentTime = models.CharField(max_length=200)
