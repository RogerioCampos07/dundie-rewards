import argparse

from dundie.core import load


def main():
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards",
        epilog="Enjoy and use with cautions",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send"),
        default="help",
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="filepath to load",
        default=None,
    )

    args = parser.parse_args()

    if args.subcommand == "load":
        result = load(args.filepath)
        header = ['name','dept','role','e-mail']
        for person in result:
            print('-'*50)
            for key, value in zip(header,person.split(',')):
                print(f"{key} -> {value.strip()}")

