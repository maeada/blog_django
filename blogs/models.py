from django.db import models

#https://docs.djangoproject.com/en/5.2/ref/contrib/auth/
from django.contrib.auth.models import User

# Create your models here.
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#django.db.models.FileField
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='uploads', default='no_picture')
    birthdate = models.DateField(blank=True, null=True) # need to add 'blank' and 'null'
    created = models.DateTimeField(auto_now_add=True) #object is first created. 
    updated = models.DateTimeField(auto_now=True) # every time the object is saved. “last-modified”

    def __str__(self):
        return f"Profile of {self.user.username}"
    
# u = User.objects.get(username="bulakorn")
# print(u)