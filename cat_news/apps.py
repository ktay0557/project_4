from django.apps import AppConfig


class CatNewsConfig(AppConfig):
    """
    Provides the primary key type for the cat_news app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cat_news'
