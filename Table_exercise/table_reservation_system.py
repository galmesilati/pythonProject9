import datetime
from Table_exercise.table import Table
from Table_exercise.table_exceptions import *

class TableReservationSystem:
    def __init__(self, restaurant_name: str, time_limit: int):
        self._time_limit = time_limit
        self._restaurant_name = restaurant_name
        self._collection_of_table: dict[int, Table] = dict()

    def get_time_limit(self):
        return self._time_limit

    def set_time_limit(self, new_time_limit: int):
        self._time_limit = new_time_limit

    def get_restaurant_name(self):
        return self._restaurant_name

    def add_table(self, table_id: int, number_of_seats: int, location:str):
        self._collection_of_table[table_id] = Table(table_id, number_of_seats,self._time_limit,location)

    def reserv_a_table(self, table_id: int, guests_number: int):
        if self._collection_of_table[table_id].get_number_of_seats() < guests_number:
            raise InvalidGuestsNum()
        if not table_id in self._collection_of_table:
            raise TableNotExecit
        self._collection_of_table[table_id].add_people(guests_number)


    def release_a_table(self, table_id:int):
        self._collection_of_table[table_id].clear_table()








    # def get_tables_with_less_minutes(self, seats_number:int, minute: datetime.datetime.minute):
    #     for table in self._collection_of_table.items():
    #     # table_available_time = dict()
    #     # for table in self._collection_of_table.items():
    #     #     table_available_time[table] = Table.time_left(time_left)

    # def get_tables_with_less_minutes(self, seats_number:int, time_left: datetime):
    #     for table in self._collection_of_table:
    #         if table["table_id"] > Table.get_when_availble(time_left):
    #             return True, table
    #         else:
    #             return False








