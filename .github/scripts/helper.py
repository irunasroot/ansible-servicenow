"""
Helper script for GitHub Actions
"""

#!/usr/bin/env python3

from pathlib import Path
from argparse import ArgumentParser

import yaml
import requests


class VersionMismatch(Exception):
    """Custom Exception"""


parser = ArgumentParser(
    description="Python helper script to assist in GitHub Actions",
)

actions = parser.add_subparsers(
    title="Action to run",
    description="Various actions this program is able to execute",
    dest="action",
    required=True,
)

published_version = actions.add_parser(
    "published-version", help="Get the current published version of the collection"
)

published_version.add_argument(
    "--url",
    help="The base URL to the galaxy hub. Default: https://galaxy.ansible.com",
    default="https://galaxy.ansible.com",
)

published_version.add_argument(
    "--verify",
    help="Verify SSL certificate. Default: True",
    action="store_true",
    default=True,
)

local_version = actions.add_parser(
    "local-version",
    help="Read galaxy.yml file and get the local version of the collection",
)

local_version.add_argument(
    "--file",
    help="The path to the galaxy.yml file to read: Default: galaxy.yml",
    default="galaxy.yml",
    required=True,
)

compare_versions = actions.add_parser(
    "compare-versions",
    help="Compare semantic version of the currently published version and the local version",
)

compare_versions.add_argument(
    "--published-version", help="The published version at the galaxy hub", required=True
)

compare_versions.add_argument(
    "--local-version", help="The local version from galaxy.yml", required=True
)


def get_published_version(url, verify):
    """Get the collection's published version from the provided galaxy server"""

    response = requests.get(
        (
            f"{url}/api/v3/plugin/ansible/content/published/"
            "collections/index/irunasroot/servicenow/versions/"
        ),
        params={"limit": 1, "offset": 0},
        verify=verify,
        timeout=30,
    )

    response.raise_for_status()
    data = response.json()

    return data["data"][0]["version"]


def get_local_version(file: Path):
    """Get the collection's published version from the provided galaxy.yml file"""

    with file.open("r") as f:
        data = yaml.safe_load(f)

    return data["version"]


def compare_semantic_versions(published, local):
    """Compare semantic versioning"""
    published = tuple(map(int, published.split(".")))
    local = tuple(map(int, local.split(".")))
    return local <= published


if __name__ == "__main__":
    args = parser.parse_args()

    match args.action:
        case "published-version":
            print(get_published_version(args.url, args.verify))
        case "local-version":
            print(get_local_version(Path(args.file)))
        case "compare-versions":
            mismatch = compare_semantic_versions(
                args.published_version, args.local_version
            )
            if mismatch:
                raise VersionMismatch(
                    (
                        "There's a mismatch issue between the published version "
                        "({args.published_version}) and local version ({args.local_version})."
                    )
                )
            print("No version mismatch issues detected")
