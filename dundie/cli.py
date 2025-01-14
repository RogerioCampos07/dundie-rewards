import argparse
from dundie.core import load

def main():
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards",
        epilog="Enjoy and use with cautions"
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load","show","send"),
        default="help"

    )
    parser.add_argument(
        "filepath",
        type=str,
        help="filepath to load",
        default=None

    )

    args = parser.parse_args()

    print("vou conseguir")
