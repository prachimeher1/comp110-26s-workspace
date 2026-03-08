"""This exercise will plan a cozy tea party."""

__author__: str = "730669446"


def main_planner(guests: int) -> None:
    """Summary of tea party planning."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    totCost: float = cost(
        tea_count=tea_bags(people=guests), treat_count=treats(people=guests)
    )
    print("Cost: $" + str(totCost))


def tea_bags(people: int) -> int:
    """Function will calculate the number of teabags needed."""
    return people * 2


def treats(people: int) -> int:
    """Function will calculate the number of treats needed."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Function will calculate the cost of the tea bags and treats."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
