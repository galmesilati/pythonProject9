# 1
import string
from datetime import datetime, timedelta
import re

my_try_list_lower = ["a", "d", "f"]
my_ter_list_upper = ["A", "F", "R"]


def letters_index(my_letters: list[str]) -> list:
    my_ascii_list = list(string.ascii_lowercase)
    my_map_list = list(map(lambda l: l.lower(), my_letters))
    new_list = list(map(lambda l: my_ascii_list.index(l) + 1, my_map_list))
    return new_list


print(letters_index(my_try_list_lower))
print(letters_index(my_ter_list_upper))


# 2

def remove_vowels(text: str) -> str:
    vol = "aAeEiIoOuU"
    word = "".join(filter(lambda t: t not in vol, text))
    return word


# 3
def map_day(dates: list) -> list:
    date_map = map(lambda date_str: datetime.strptime(date_str, "%d-%m-%Y"), dates)
    date_filter = filter(lambda date: date.weekday() not in (4, 5), date_map)
    return list(date_filter)


# 4
def sort_text(my_list: list) -> list:
    return sorted(my_list, key=len)


# 5
# def sorted_dict(my_dict_list: list[dict]) -> list:
#     new_dict_list = list(sorted(my_dict_list, key=lambda name: name['name']))
#     return new_dict_list

# 5
def h_m(str2: str) -> list:
    w = re.compile("(.*h|.*m)")
    result = w.findall(str2)
    return result


def sorted_dict(dict_list: list[dict]) -> list[dict]:
    new_dict_list_1 = list(sorted(dict_list, key=lambda n: n['name']))
    new_dict_list_2 = list(sorted(new_dict_list_1, key=lambda n: n['delays']))


# 6
def filter_word(words_list: list[str]) -> list:
    my_filter_words = list(filter(lambda w: w.count("a") > 2, words_list))
    return my_filter_words


if __name__ == '__main__':
    dates = ['12-12-2021', '18-12-2021', '19-12-2021']
    buses = [
        {
            "delays": ['1h 20m', '25m', '3h', '2h 1m'],
            "status": 'bad',
            "name": "Jacob",
            "route_num": 560
        },
        {
            "delays": ['20m', '5m', '3h'],
            "status": 'great',
            "name": "Moshe",
            "route_num": 769
        },
        {
            "delays": ['2h 3m'],
            "status": 'good',
            "name": "Jack",
            "route_num": 766
        },
        {
            "delays": ['6h'],
            "status": 'great',
            "name": "Mark",
            "route_num": 876
        },
        {
            "delays": ['2h 3m'],
            "status": 'good',
            "name": "Anna",
            "route_num": 456
        },
    ]

    print(remove_vowels("today is Monday"))
    print(letters_index(my_try_list_lower))
    print(letters_index(my_ter_list_upper))
    print(sort_text(['gal', 'chen', 'valeria', 'herut']))
    print(map_day(dates))
    # print(sorted_dict(buses))
    print(filter_word(["apple", "ananas", "banana", "pear"]))
