from django.apps import AppConfig


class FavoritebeautyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'favoritebeauty'

    #def ready(self):
    #    from .ap_scheduler import start
    #    start()
