from django.db import models
import datetime as dt

#https://docs.djangoproject.com/en/5.2/ref/contrib/auth/
from django.contrib.auth.models import User

# Create your models here.
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#django.db.models.FileField
class Profile(models.Model):
    """The user profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='uploads', default='no_picture.png')
    birthdate = models.DateField(blank=True, null=True) # need to add 'blank' and 'null'
    created = models.DateTimeField(auto_now_add=True) #object is first created. 
    updated = models.DateTimeField(auto_now=True) # every time the object is saved. “last-modified”

    def __str__(self):
        return f"Profile of {self.user.username}" #, age: {self.calculate_age}"
    
    def calculate_age(self):
        """Calculates the age in years based on a given birthdate."""
        today = dt.date.today()
        age = today.year - self.birthdate.year

        # Adjust age if the birthday has not yet occurred in the current year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age
    

    
# u = User.objects.get(username="bulakorn")
# print(u)

class Content(models.Model):
    """The blog content user post."""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)#เมื่อInstanceของProfile(PK) ถูกลบ InstanceของContent(FK)ก็จะถูกลบด้วย
    subject = models.CharField(max_length=100)
    content = models.TextField()
    picture = models.ImageField(upload_to='pictures', default='no_picture.png')
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Subject: {self.subject} (date: {self.created.strftime('%d/%m/%Y')})"

# class Comment(models.Model):
#     content = models.ForeignKey(Content, on_delete=models.CASCADE)