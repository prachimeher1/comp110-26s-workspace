"""Dictionary Functions"""

__author__ = "730669446"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert keys and values of a dictionary."""
    result: dict[str, str] = {}

    keys: list[str] = list(input_dict.keys())
    i: int = 0

    while i < len(keys):
        key: str = keys[i]
        value: str = input_dict[key]

        if value in result:
            raise KeyError("ERROR!")

        result[value] = key
        i = i + 1

    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Return the color that appears the most frequently"""
    color_count: dict[str, int] = {}

    names: list[str] = list(colors.keys())
    i: int = 0

    while i < len(names):
        name: str = names[i]
        color: str = colors[name]

        if color in color_count:
            color_count[color] = color_count[color] + 1
        else:
            color_count[color] = 1

        i = i + 1

    color_list: list[str] = list(color_count.keys())
    j: int = 0

    most_common_color: str = ""
    highest_count: int = 0

    while j < len(color_list):
        color: str = color_list[j]

        if color_count[color] > highest_count:
            most_common_color = color
            highest_count = color_count[color]

        j = j + 1

    return most_common_color


def count(values: list[str]) -> dict[str, int]:
    """Count how many times each value appears in a list."""
    result: dict[str, int] = {}

    i: int = 0

    while i < len(values):
        item: str = values[i]

        if item in result:
            result[item] = result[item] + 1
        else:
            result[item] = 1

        i += 1

    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group words by their first letter."""
    result: dict[str, list[str]] = {}

    i: int = 0

    while i < len(words):
        word: str = words[i]
        first_letter: str = word[0].lower()

        if first_letter.isalpha():
            if first_letter in result:
                result[first_letter].append(word)
            else:
                result[first_letter] = [word]

        i = i + 1

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Update attendance log with a student's attendance."""
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
