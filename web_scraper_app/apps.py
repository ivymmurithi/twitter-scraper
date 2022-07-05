from django.apps import AppConfig


class WebScraperAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_scraper_app'
    verbose_name = "web_scrapper"

    def ready(self):
        import web_scraper_app.signals