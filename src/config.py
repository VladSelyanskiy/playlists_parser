from pydantic import BaseModel, Field
import os


class Config(BaseModel):

    PATH_FAVICON: str = Field(default=os.path.join("src", "static", "favicon.ico"))
    PATH_HTML: str = Field(default=os.path.join("src", "static", "index.html"))


config = Config()
