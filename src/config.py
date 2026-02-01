from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):

    PATH_FAVICON: str = os.path.join("src", "static", "favicon.ico")
    PATH_HTML: str = os.path.join("src", "static", "index.html")


settings = Settings()
