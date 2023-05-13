from typing import List


def get_instructions(file_path: str, beginning: str, ending: str) -> List[str]:
    with open(file_path, "r") as f:
        text = f.read()
        instruction_str = _find_between(text, beginning, ending)
        return [line for line in instruction_str.split("\n") if line != ""]


def _find_between(s: str, first: str, last: str) -> str:
    start = s.index(first) + len(first)
    try:
        end = s.index(last, start)
    except ValueError as e:
        end = len(s)

    return s[start:end]
