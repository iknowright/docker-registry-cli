from docker_registry_cli import out
from docker_registry_cli.registry import api


class ListRepo:
    """Listing repositories"""

    def __call__(self):
        out.write("\n".join(api.list_repos().json()["repositories"]))
