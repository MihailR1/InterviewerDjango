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


settings = Settings()
