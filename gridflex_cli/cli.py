import argparse
from pathlib import Path

from gridflex.main import duplicate_project


def main(argv=None):
    parser = argparse.ArgumentParser(prog="gridflex-cli", description="GridFlex utility CLI")
    sub = parser.add_subparsers(dest="command")

    dup = sub.add_parser("duplicate", help="Duplicate project to a new directory")
    dup.add_argument("target_dir", type=Path)
    dup.add_argument("package_name")

    args = parser.parse_args(argv)

    if args.command == "duplicate":
        duplicate_project(args.target_dir, args.package_name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
