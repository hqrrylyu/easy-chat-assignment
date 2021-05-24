# flake8: noqa: F401, F403
from .base import *

DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", engine="django.db.backends.postgresql"),
}

DATABASES["default"]["CONN_MAX_AGE"] = 50
