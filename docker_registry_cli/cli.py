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
                "name": ["init"],
                "help": "init project configuration",
                "func": commands.Print,
            },
            {
                "name": ["commit", "c"],
                "help": "create new commit",
                "func": commands.Print,
                "arguments": [
                    {
                        "name": ["--retry"],
                        "action": "store_true",
                        "help": "retry last commit",
                    },
                    {
                        "name": "--dry-run",
                        "action": "store_true",
                        "help": "show output to stdout, no commit, no modified files",
                    },
                ],
            },
            {
                "name": "ls",
                "help": "show available projects",
                "func": commands.Print,
            },
            {"name": "example", "help": "show commit example", "func": commands.Print,},
            {
                "name": "info",
                "help": "show information about the cz",
                "func": commands.Print,
            },
            {"name": "schema", "help": "show commit schema", "func": commands.Print},
            {
                "name": "bump",
                "help": "bump semantic version based on the git log",
                "func": commands.Print,
                "arguments": [
                    {
                        "name": "--dry-run",
                        "action": "store_true",
                        "help": "show output to stdout, no commit, no modified files",
                    },
                    {
                        "name": "--files-only",
                        "action": "store_true",
                        "help": "bump version in the files from the config",
                    },
                    {
                        "name": "--local-version",
                        "action": "store_true",
                        "help": "bump only the local version portion",
                    },
                    {
                        "name": ["--changelog", "-ch"],
                        "action": "store_true",
                        "default": False,
                        "help": "generate the changelog for the newest version",
                    },
                    {
                        "name": ["--no-verify"],
                        "action": "store_true",
                        "default": False,
                        "help": "this option bypasses the pre-commit and commit-msg hooks",
                    },
                    {
                        "name": "--yes",
                        "action": "store_true",
                        "help": "accept automatically questions done",
                    },
                    {
                        "name": "--tag-format",
                        "help": (
                            "the format used to tag the commit and read it, "
                            "use it in existing projects, "
                            "wrap around simple quotes"
                        ),
                    },
                    {
                        "name": "--bump-message",
                        "help": (
                            "template used to create the release commit, "
                            "useful when working with CI"
                        ),
                    },
                    {
                        "name": ["--prerelease", "-pr"],
                        "help": "choose type of prerelease",
                        "choices": ["alpha", "beta", "rc"],
                    },
                    {
                        "name": ["--increment"],
                        "help": "manually specify the desired increment",
                        "choices": ["MAJOR", "MINOR", "PATCH"],
                    },
                    {
                        "name": ["--check-consistency", "-cc"],
                        "help": (
                            "check consistency among versions defined in "
                            "project configuration and version_files"
                        ),
                        "action": "store_true",
                    },
                    {
                        "name": ["--annotated-tag", "-at"],
                        "help": "create annotated tag instead of lightweight one",
                        "action": "store_true",
                    },
                    {
                        "name": ["--changelog-to-stdout"],
                        "action": "store_true",
                        "default": False,
                        "help": "Output changelog to the stdout",
                    },
                ],
            },
            {
                "name": ["changelog", "ch"],
                "help": (
                    "generate changelog (note that it will overwrite existing file)"
                ),
                "func": commands.Print,
                "arguments": [
                    {
                        "name": "--dry-run",
                        "action": "store_true",
                        "default": False,
                        "help": "show changelog to stdout",
                    },
                    {
                        "name": "--file-name",
                        "help": "file name of changelog (default: 'CHANGELOG.md')",
                    },
                    {
                        "name": "--unreleased-version",
                        "help": (
                            "set the value for the new version (use the tag value), "
                            "instead of using unreleased"
                        ),
                    },
                    {
                        "name": "--incremental",
                        "action": "store_true",
                        "default": False,
                        "help": (
                            "generates changelog from last created version, "
                            "useful if the changelog has been manually modified"
                        ),
                    },
                    {
                        "name": "--start-rev",
                        "default": None,
                        "help": (
                            "start rev of the changelog."
                            "If not set, it will generate changelog from the start"
                        ),
                    },
                ],
            },
            {
                "name": ["check"],
                "help": "validates that a commit message matches the project schema",
                "func": commands.Print,
                "arguments": [
                    {
                        "name": "--commit-msg-file",
                        "help": (
                            "ask for the name of the temporal file that contains "
                            "the commit message. "
                            "Using it in a git hook script: MSG_FILE=$1"
                        ),
                        "exclusive_group": "group1",
                    },
                    {
                        "name": "--rev-range",
                        "help": "a range of git rev to check. e.g, master..HEAD",
                        "exclusive_group": "group1",
                    },
                    {
                        "name": ["-m", "--message"],
                        "help": "commit message that needs to be checked",
                        "exclusive_group": "group1",
                    },
                ],
            },
            {
                "name": ["version"],
                "help": (
                    "get the version of the installed project or the current project"
                    " (default: installed project)"
                ),
                "func": commands.Print,
                "arguments": [
                    {
                        "name": ["-p", "--project"],
                        "help": "get the version of the current project",
                        "action": "store_true",
                        "exclusive_group": "group1",
                    },
                    {
                        "name": ["-c", "--project"],
                        "help": "get the version of the installed project",
                        "action": "store_true",
                        "exclusive_group": "group1",
                    },
                    {
                        "name": ["-v", "--verbose"],
                        "help": (
                            "get the version of both the installed project "
                            "and the current project"
                        ),
                        "action": "store_true",
                        "exclusive_group": "group1",
                    },
                ],
            },
        ],
    },
}


def main():
    parser = cli(data)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    print(args, vars(args))
    args.func("test")()


if __name__ == "__main__":
    main()
