from typing import List

import PySimpleGUI as sg

WINDOW_LOCATION_MAPPING = {"TOP": (500, 0), "MIDDLE": (500, 400), "BOTTOM": (500, 800)}


def sticky_window(window_location_option: str, instructions: List[str]) -> None:
    window_locations = WINDOW_LOCATION_MAPPING.get(window_location_option.upper())
    instruction_index = 0
    layout = [
        [
            sg.T(
                instructions[0],
                font=("Arial", 14),
                text_color="black",
                key="instruction",
            )
        ],
        [sg.Button("Prev"), sg.Button("Next")],
    ]
    window = sg.Window(
        "Kata", layout, keep_on_top=True, location=window_locations, finalize=True
    )
    window.bind("<Right>", "-NEXT-")
    window.bind("<Left>", "-PREV-")
    window.bind("<q>", "Exit")
    window["Prev"].update(disabled=True)

    while True:
        event, values = window.read()

        if event in ("Exit", sg.WINDOW_CLOSED):
            break

        elif event in ("Prev", "-PREV-"):
            if 0 >= (instruction_index - 1):
                instruction_index = instruction_index - 1
                instruction = instructions[instruction_index]
                window["instruction"].update(instruction)

        elif event in ("Next", "-NEXT-"):
            if (instruction_index + 1) < len(instructions):
                instruction_index = instruction_index + 1
                instruction = instructions[instruction_index]
                window["instruction"].update(instruction)

        if instruction_index == 0:
            window["Prev"].update(disabled=True)
        else:
            window["Prev"].update(disabled=False)

        if instruction_index == len(instructions) - 1:
            window["Next"].update(disabled=True)
        else:
            window["Next"].update(disabled=False)

    window.close()
