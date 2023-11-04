from django.apps import AppConfig


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'

    # every time images app is loaded import signals
    # signals --> send signal if num of liked_users changed
    def ready(self) -> None:
        import images.signals