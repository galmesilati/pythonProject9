import datetime
class DatesOfTheMonth:
    def __init__(self, start=datetime.date.today()):
        self.start_from = start
        if type(self.start_from) != datetime.date:
            raise DateTypeError

    def get_start(self):
        return self.start_from
    def __iter__(self):
        self.counter = self.start_from
        return self

    def __next__(self):
        if self.counter.month != self.start_from.month:
            raise StopIteration()
        curr = self.counter
        self.counter += datetime.timedelta(days=1)
        return curr



class DateTimeError(Exception):
    def __init__(self):
        super(DateTimeError, self).__init__()


class DateTypeError(DateTimeError):
    def __init__(self):
        super(DateTypeError, self).__init__()


if __name__ == '__main__':
    while True:
        try:
            year = int(input("insert the year: "))
            month = int(input("insert the month: "))
            day = int(input("insert the day: "))
            # my_date = input("insert your date: ")
            my_date = datetime.date(year, month, day)
            my_dt = DatesOfTheMonth(my_date)
            for i in my_dt:
                print(i)
            break
        except DateTypeError:
            print("your date is not in the correct format")
            break
        except ValueError as e:
            print("the date you entered is incorrect ")
            break
        except Exception as e:
            print(e)
            break
        finally:
            print("Exit")
            break


    # for date in my_dt:
    #     print(date)
    #     try:
    #         if type(my_dt.get_start()) != datetime:
    #             raise DateTypeError(my_dt)
    #     except DateTypeError:
    #         print("your date is not in the correct format")
