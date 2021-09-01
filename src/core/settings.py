from pydantic import BaseSettings, DirectoryPath


class Settings(BaseSettings):
    webapp_static_path: DirectoryPath = "core/views/static/"
