# https://docs.djangoproject.com/en/5.2/topics/db/models/#overriding-model-methods
from django.db import models
import datetime as dt
from django.utils import timezone

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
        return f"Profile of {self.user.username}, age: {self.calculate_age()}"
        # return f"Profile of {self.user.username}" 

    def calculate_age(self):
        """Calculates the age in years based on a given birthdate."""
        if not self.birthdate:
            return None     
        
        today = dt.date.today()
        age = today.year - self.birthdate.year

        # Adjust age if the birthday has not yet occurred in the current year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age
    
    # def save(self, *args, **kwargs):
    #     """Overriding predefined model methods.
    #     This function is advantage when you want to save 'field' to database'
    #     """
    #     self.calculate_age()    #  This line not need because 'age' is not 'field'
    #     return super().save()
    
    
# u = User.objects.get(username="bulakorn")
# print(u)
def get_default_catagory():
    """Gets or creates the default 'General' category object
    and returns its primary key (pk).
    This function will try to find a category named 'General' and 
        if it doesn't exist, it will create it.
    # The .get_or_create() method returns a tuple of (object, created_boolean)
    # We want the primary key (pk) of the object, so we access it with [0].pk
    # It is recommended to use the primary key for the default value of a ForeignKey.    
    """
    # Use .get_or_create with the correct field name ('name')
    catagory_obj, created = Catagory.objects.get_or_create(name='General')
    print(f"catagory_obj: {catagory_obj}, created: {created}")
    return catagory_obj.pk
    # return Catagory.objects.get_or_create(name='General')[0].pk


class Content(models.Model):
    """The blog content user post."""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)#เมื่อInstanceของProfile(PK) ถูกลบ InstanceของContent(FK)ก็จะถูกลบด้วย
    subject = models.CharField(max_length=100)
    content = models.TextField()
    picture = models.ImageField(upload_to='pictures', default='no_picture.png')
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)
    # Add catagory field
    # enclose model_name with ' ' because prevent the Error from Catagory model is created below the Content model.
    catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE,
                                  default=get_default_catagory) # only function name exclude parentheses here!

    def __str__(self):
        return f"{self.subject} (by: {self.profile.user.username}) (date: {self.created.strftime('%d/%m/%Y')})"

   
class Comment(models.Model):
    """This model serve the comment of user about content on website."""
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(blank=True)  
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.profile.user.username} comment to {self.content.subject} on date {self.created.date()}"
    
    def save(self, *args, **kwargs):
        """"Overriding predefined model methods.
        This function is advantage when you want to save 'field' to database'
        """
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)
    
class Catagory(models.Model):
    """Catagory of contents."""
    CATAGORY_NAME = {'MATH': 'Mathematics',
                     'TECH': 'Technology',
                     'CODING': 'Coding',
                     'AI': 'Artificial Intelligence',
                     'ML': 'Machine Learning',
                     'PROMPT': 'Prompt Engineering',
                     'WEB': 'Web Development',
                     'TRADING': 'Trading and Finance',
                     'General': 'General'                    
                     }
    # This field name must match what you use in get_or_create
    name = models.CharField(max_length=20, choices=CATAGORY_NAME)

    def __str__(self):
        return f"Catagory: {self.name}"