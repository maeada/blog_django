##  ทุกครั้งที่เรา   run command 'manage.py runserver' ไฟล์นี้(apps.py) จะถูกexcuteทุกครั้ง
from django.apps import AppConfig


class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'

    def ready(self):
        """"""
        import blogs.signals    #blogs/signals.py
