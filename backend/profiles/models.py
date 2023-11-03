from django.db import models
from django.core import validators
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/profiles/", null=True, blank=True,default="images/profiles/default-profile.jpg",validators=[validators.FileExtensionValidator(['jpg','jpeg', 'gif', 'png',])])
    created = models.DateTimeField(auto_now_add=True)
    follows = models.ManyToManyField("self",related_name="followed_by",symmetrical=False,blank=True)

    def __str__(self):
        return self.user.username
    

def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([user_profile.id])
        user_profile.save()

post_save.connect(create_profile,sender=User)