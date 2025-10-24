from django.contrib import admin
from .models import Profile, Content, Comment, Catagory

# Register your models here.
# admin.site.register(Profile)
# admin.site.register(Content)
# admin.site.register(Comment)

# Register multple models at once time
my_models_to_regiter = [Profile, Content, Comment, Catagory]
admin.site.register(my_models_to_regiter)



