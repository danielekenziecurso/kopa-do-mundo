from datetime import datetime
from exceptions import *


def data_processing(data_dict: dict):
    titles_value = data_dict.get("titles")
    if titles_value is not None and titles_value < 0:
        raise NegativeTitlesError("titles cannot be negative")

    first_cup_date = int(data_dict["first_cup"][:4])
    years_cup = []
    data_cup = datetime.now().year
    for year in range(1930, data_cup, 4):
        years_cup.append(year)
    if first_cup_date < 1930 or first_cup_date not in years_cup:
        raise InvalidYearCupError("there was no world cup this year")

    total_cups = (data_cup - first_cup_date)/4
    if data_dict["titles"] > total_cups:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
