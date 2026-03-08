"""EX04 - List Utility Functions"""

__author__ = "730669446"


def all(input: list[int], num: int) -> bool:
    """Checks if all values are equal to some integer"""
    if len(input) == 0:  # if list is empty return False
        return False
    i: int = 0

    while i < len(
        input
    ):  # checking each index of the list, if one does not equal the int then return False
        if input[i] != num:
            return False
        i = i + 1
    return True


def max(input: list[int]) -> int:
    """Return largest index"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    maximum: int = input[0]
    j: int = 0

    while j < len(input):  # checking if any value is greater than index 0 value
        if input[j] > maximum:
            maximum = input[j]
        j = j + 1
    return maximum


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists are equal"""
    if len(list1) != len(list2):  # if the lists are not of the same length return false
        return False
    k: int = 0
    while k < len(list1):
        if list1[k] != list2[k]:  # if any indexes are not the same then return false
            return False
        k = k + 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Add elements of list2 to list1"""
    l: int = 0
    while l < len(list2):
        list1.append(list2[l])
        l = l + 1
