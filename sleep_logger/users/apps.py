from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "sleep_logger.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import sleep_logger.users.signals  # noqa F401
        except ImportError:
            pass
