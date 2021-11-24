import questionary

from docker_registry_cli import out
from docker_registry_cli.registry import api


class Remove:
    """Remote a image tag from registry"""

    custom_style_dope = questionary.Style(
        [
            ("separator", "fg:#6C6C6C"),
            ("qmark", "fg:#FF9D00 bold"),
            ("question", ""),
            ("selected", "fg:#5F819D"),
            ("pointer", "fg:#FF9D00 bold"),
            ("answer", "fg:#5F819D bold"),
        ]
    )

    def __call__(self):
        repo = questionary.rawselect(
            "Repository to delete", choices=api.list_repos().json()["repositories"]
        ).ask()
        tag = questionary.rawselect(
            f"[{repo}] tag to delete", choices=api.list_repo_tags(repo).json()["tags"]
        ).ask()
        manifest_resp = api.get_detail_manifest(repo, tag)
        target_digest = manifest_resp.headers.get("Docker-Content-Digest")
        delete_resp = api.delete_image_reference(repo, target_digest)
        if delete_resp.status_code == 202:
            out.success(f"Successfully delete image/tag {repo}:{tag}")
        else:
            out.error("Failed")
