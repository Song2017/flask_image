import os
import sys
import threading

from cached_property import cached_property
from singleton_decorator import singleton


@singleton
class NomadConstants:

    @cached_property
    def project_dir(self) -> str:
        return os.path.dirname(__file__).replace("app", "").replace(
            "/utils", "")

    def project_file(self, filename) -> str:
        return os.path.join(self.project_dir, filename)

    @cached_property
    def server_url(self) -> str:
        return self.openapi_data["servers"][0]["url"]  # assume first url

    @cached_property
    def is_dev_local(self) -> bool:
        """ We assume every NomadConnector developer all use Mac. """
        return sys.platform == "darwin"

    @cached_property
    def thread_storage(self) -> dict:
        storage = threading.local()
        storage.requests = {}
        return storage.requests


constants = NomadConstants()
project_dir = constants.project_dir
project_file = constants.project_file
__all__ = [
    "project_dir",
    "project_file",
    "constants",
]
