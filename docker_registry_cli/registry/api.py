import traceback

import requests
from loguru import logger

from docker_registry_cli.config import Config


def request(method: str, path: str, headers: dict = None):
    try:
        response = requests.request(method, f"{Config.REGISTRY_URL}/v2/{path}", headers=headers, auth=(Config.USERNAME, Config.PASSWORD))
        logger.debug(f"{method} {path} -> {response.status_code}")
        return response
    except requests.exceptions.Timeout as error:
        logger.warning(f"UNAVAILABLE: Connection Timeout {error}")
    except requests.exceptions.ConnectionError as error:
        logger.warning(f"UNAVAILABLE: Connection Error {error}")
    except ConnectionRefusedError as error:
        logger.warning(f"UNAVAILABLE: Connection Refused Error {error}")
    except requests.exceptions.MissingSchema:
        logger.warning(f"UNAVAILABLE: URL Schema Error {traceback.format_exc()}")


def list_repos():
    return request("GET", "_catalog")


def list_repo_tags(repo: str):
    return request("GET", f"{repo}/tags/list")


def get_detail_manifest(repo: str, tag: str):
    headers = {"Accept": "application/vnd.docker.distribution.manifest.v2+json"}
    return request("GET", f"{repo}/manifests/{tag}", headers)


def delete_image_reference(repo: str, digest: str):
    return request("DELETE", f"{repo}/manifests/{digest}")
