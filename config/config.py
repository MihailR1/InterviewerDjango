from typing import Literal

from environs import Env


class Settings:
    env = Env()
    env.read_env()

    POSTGRES_DB = env.str("POSTGRES_DB")
    POSTGRES_USER = env.str("POSTGRES_USER")
    POSTGRES_HOST = env.str("POSTGRES_HOST")
    POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
    POSTGRES_PORT = env.int("POSTGRES_PORT")

    SECRET_KEY = env.str("SECRET_KEY")
    DEBUG = env.bool("DEBUG")
    MODE: Literal["DEV", "TEST", "PROD"] = env.str("MODE")

    ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

    SENTRY_KEY = env.str("SENTRY_TOKEN")
    SENTRY_PROJECT_NAME = env.str("SENTRY_PROJECT_NAME")

    admin_elements_per_page = 50
    admin_preview_text_limit = 150


settings = Settings()
