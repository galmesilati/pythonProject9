import datetime
from  datetime import timedelta
from table_exceptions import *
# format_time = "%H:%M"
class Table:
    def __init__(self,table_id: int, number_of_seats: int, time_limit: int, location:str, occuiped_seats=0):
        if location in ["bar", "terrace", "indoors", "floor_number", "vip_room", "near_toilet", "next_exit", "near_kitchen"]:
            self._location = location
        else:
            return
        self._occupied_seats = occuiped_seats
        self._time_limit = time_limit
        self._reservation_start_time: datetime = None
        self._number_of_seats = number_of_seats
        self._table_id = table_id

    def get_time_limit(self):
        return self._time_limit

    def set_time_limit(self, new_time_limit: int):
        self._time_limit = new_time_limit

    def get_reservation_start_time(self):
        return self._reservation_start_time

    def get_occuiped_seats(self):
        return self._occupied_seats

    def get_number_of_seats(self):
        return self._number_of_seats

    def get_table_id(self):
        return self._table_id

    def is_available(self):
        if self._occupied_seats > 0:
            return False
        else:
            return True

    def add_people(self, number_guests:int):
        if self._occupied_seats != 0:
            raise TableAlreadyReserved()
        if self._number_of_seats < number_guests:
            raise InvalidGuestsNum()
        self._reservation_start_time = datetime.datetime.now()
        self._occupied_seats += number_guests

    def time_left(self):
        return datetime.datetime.now() - self._reservation_start_time + timedelta(minutes= self._time_limit)

    def get_when_availble(self):
        return datetime.datetime.now() + self.time_left()

    def clear_table(self):
        if self._occupied_seats == 0:
            raise TableIsFree()
        self._reservation_start_time = None
        self._occupied_seats = 0



