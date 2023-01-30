from table import Table
from table_reservation_system import TableReservationSystem
import datetime

if __name__ == '__main__':
    system = TableReservationSystem("KYOTO", 105)
    system.add_table(12, 4, "terrace")
    system.add_table(11,2, "vip_room")
    system.add_table(10, 3, "near_toilet")

    print(system.reserv_a_table(11,2))
    print(5)
    print(system.reserv_a_table(12,4))
    print(6)
    system.release_a_table(10)
    print(system._collection_of_table[10]._occupied_seats)
    print(7)
    print(system._collection_of_table[11].time_left())
    print(8)
    print(system._collection_of_table[12].get_when_availble())
    # print(system.get_tables_with_less_minutes(1,90))
