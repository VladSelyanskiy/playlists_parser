from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    class Static:
        PATH_FAVICON: str = os.path.join("src", "static", "favicon.ico")
        PATH_HTML: str = os.path.join("src", "static", "index.html")

    class APIKeys:
        URL_API_KEY: str = "https://api.music.yandex.net"


settings = Settings()
conf_static = Settings.Static()
conf_api = Settings.APIKeys()
