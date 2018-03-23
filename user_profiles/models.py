
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
  
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  first_name = models.CharField(max_length=32, blank=True, null=True)
  last_name = models.CharField(max_length=32, blank=True, null=True)
  
  image_url = models.URLField(blank=True, null=True)
  
  city = models.CharField(max_length=32, blank=True, null=True)
  state = models.CharField(
    max_length=32,
    blank=True,
    null=True,
    verbose_name="State or Province"
  )
  country = models.CharField(max_length=32, blank=True, default='US', null=True)
  
  date_of_birth = models.DateField(blank=True, null=True)
  
  bio = models.TextField(blank=True, null=True)
  
  GENDER_CHOICES = [
    ("Male", 'M'),
    ("Female", 'F')
  ]
  gender = models.CharField(
    max_length=1,
    blank=True,
    choices=GENDER_CHOICES,
    null=True
  )
  
  join_date = models.DateField(auto_now_add=True)
  
  friends = models.ManyToManyField('self', blank=True)
  
  def __str__(self):
    return "Profile: {}".format(self.user)