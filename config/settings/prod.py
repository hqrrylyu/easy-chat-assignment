# flake8: noqa: F401, F403
from .base import *

DATABASES = {
    "default": env.dj_db_url("DATABASE_URL"),
}

DATABASES["default"]["CONN_MAX_AGE"] = 50
