import argparse
import logging
import sys
from functools import partial

import argcomplete
from decli import cli

from docker_registry_cli import commands

logger = logging.getLogger(__name__)
data = {
    "prog": "docker-registry-cli",
    "description": (
        "docker-registry-cli is a cli tool to manage private docker registry.\n"
    ),
    "formatter_class": argparse.RawDescriptionHelpFormatter,
    "arguments": [
        {"name": "--debug", "action": "store_true", "help": "use debug mode"},
        {
            "name": ["-n", "--name"],
            "help": "use the given project (default: project)",
        },
    ],
    "subcommands": {
        "title": "commands",
        "required": True,
        "commands": [
            {
                "name": ["configure"],
                "help": "configuration docker registry url and credentials",
                "func": commands.Print,
            },
            {
                "name": ["ls"],
                "help": "listing all repositories in registry",
                "func": commands.Print,
            },
            {
                "name": ["remove", "rm"],
                "help": "remove",
                "func": commands.Print,
            },
        ],
    },
}


def main():
    parser = cli(data)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    args.func("test")()


if __name__ == "__main__":
    main()
