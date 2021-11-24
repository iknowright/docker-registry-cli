import os


class Config:
    REGISTRY_URL = os.environ.get("REGISTRY_URL", "")
    USERNAME = os.environ.get("USERNAME")
    PASSWORD = os.environ.get("PASSWORD")
