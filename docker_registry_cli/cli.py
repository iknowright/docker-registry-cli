import argparse

import argcomplete
from decli import cli

from docker_registry_cli import commands

data = {
    "prog": "docker-registry-cli",
    "description": (
        "docker-registry-cli is a cli tool to manage private docker registry.\n"
    ),
    "formatter_class": argparse.RawDescriptionHelpFormatter,
    "arguments": [
        {"name": "--debug", "action": "store_true", "help": "use debug mode"},
        {"name": ["-n", "--name"], "help": "use the given project (default: project)",},
    ],
    "subcommands": {
        "title": "commands",
        "required": True,
        "commands": [
            {
                "name": ["ls"],
                "help": "listing all repositories in registry",
                "func": commands.ListRepo,
            },
            {"name": ["remove", "rm"], "help": "remove", "func": commands.Remove,},
        ],
    },
}


def main():
    parser = cli(data)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    args.func()()


if __name__ == "__main__":
    main()
