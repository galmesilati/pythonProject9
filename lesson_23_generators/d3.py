import datetime


def my_gen(my_date= datetime.date.today()):
    counter = my_date
    while my_date.month == counter.month:
        yield counter
        counter += datetime.timedelta(days=1)

if __name__ == '__main__':
    for date in my_gen(datetime.date(2022,12,22)):
        print(date)
