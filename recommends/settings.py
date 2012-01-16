from django.conf import settings


RECOMMENDS_TASK_RUN = getattr(settings, 'RECOMMENDS_TASK_RUN', True)
RECOMMENDS_TASK_CRONTAB = getattr(settings, 'RECOMMENDS_TASK_CRONTAB', {'hour': '*/24'})
RECOMMENDS_CACHE_TEMPLATETAGS_TIMEOUT = getattr(settings, 'RECOMMENDS_CACHE_TEMPLATETAGS_TIMEOUT', 60)
RECOMMENDS_STORAGE_BACKEND = getattr(settings, 'RECOMMENDS_STORAGE_BACKEND', 'recommends.storages.DjangoOrmStorage')
