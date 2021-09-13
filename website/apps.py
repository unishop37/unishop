from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'website'


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'website'