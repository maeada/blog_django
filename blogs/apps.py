##  ทุกครั้งที่เรา   run command 'manage.py runserver' ไฟล์นี้(apps.py) จะถูกexcuteทุกครั้ง
# https://docs.djangoproject.com/en/5.2/ref/applications/
from django.apps import AppConfig   #  it uses that configuration for the application


class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'

    def ready(self):
        """"""
        import blogs.signals    #blogs/signals.py
