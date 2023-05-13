import argparse

from stick_window import sticky_window
from instruction import get_instructions


def main() -> None:
    args = _parse_args()

    instructions = get_instructions(
        file_path=args.markdown_path,
        beginning=args.beginning_part,
        ending=args.ending_part,
    )

    sticky_window(
        window_location_option=args.window_location_option, instructions=instructions
    )


def _parse_args():
    parser = argparse.ArgumentParser(
        description="Stick window with instruction from markdown."
    )
    parser.add_argument("--markdown_path", metavar="P", help="Markdown location")
    parser.add_argument(
        "--beginning_part", metavar="P", help="Ending of the instructions"
    )
    parser.add_argument(
        "--ending_part", metavar="P", help="Beginning of the instructions"
    )
    parser.add_argument(
        "--window_location_option", nargs="?", const="top", default="top"
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()
