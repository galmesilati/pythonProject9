from _datetime import datetime
# def remove_vowels(text:str) -> str:
#     vol = "a, e, i, o, u"
#     word = "".join(filter(lambda t: t not in vol, text))
#     return word
#
# if __name__ == '__main__':
#     print(remove_vowels("today is Monday"))


# dates = ['12-12-2021', '18-12-2021', '19-12-2021']

# def map_day(dates:list) -> list:
#     date_map = map(lambda date_str: datetime.strptime(date_str, "%d-%m-%Y"), dates)
#     date_filter = filter(lambda date: date.weekday() not in (4, 5),date_map)
#     return list(date_filter)
#
# if __name__ == '__main__':
#     print(map_day(['12-12-2021', '18-12-2021', '19-12-2021']))

names = ["gal", "chen", "valerya", "nadav"]

def sorted_names(text: list):
    return sorted(text, key=len)

print(sorted_names(names))




