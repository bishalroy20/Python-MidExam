"""Star Cinema"""


class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        
        
        seat = [[0 for c in range(self.cols)] for r in range(self.rows)]
        self.seats[id] = seat


    def book_seats(self, id, seat_list):
        if id in self.seats:
            for (row, col) in seat_list:
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if self.seats[id][row][col] == 0:
                        self.seats[id][row][col] = 1
                        print(f"Seat at row {row+1}, col {col+1} for show {id} has been booked.")
                    else:
                        print(f"Seat at row {row+1}, col {col+1} for show {id} is already booked.")
                else:
                    print(f"Invalid seat location: row {row+1}, col {col+1}.")
        else:
            print(f"Show ID {id} not found.")

    def view_show_list(self):
        print(f"Shows running in Hall {self.hall_no}:")
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id in self.seats:
            print(f"Available seats for show {id}:")
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.seats[id][row][col] == 0:
                        print(f"Row {row+1}, Col {col+1}")
        else:
            print(f"Show ID {id} not found.")

class Counter:
    @staticmethod
    def view_all_shows(hall):
        hall.view_show_list()

    @staticmethod
    def view_seats(hall, show_id):
        hall.view_available_seats(show_id)

    @staticmethod
    def book_tickets(hall, show_id, seats):
        hall.book_seats(show_id, seats)

    @staticmethod
    def select_option(option, hall):
        if option == 1:
            Counter.view_all_shows(hall)
        elif option == 2:
            show_id = input("Enter show ID to view available seats: ")
            Counter.view_seats(hall, show_id)
        elif option == 3:
            show_id = input("Enter show ID to book tickets: ")
            seat_count = int(input("Enter number of seats to book: "))
            seats = []
            for i in range(seat_count):
                row = int(input("Enter row number: ")) - 1
                col = int(input("Enter column number: ")) - 1
                seats.append((row, col))
            Counter.book_tickets(hall, show_id, seats)
        else:
            print("Invalid option selected.")

# a = Star_Cinema()
# a.entry_hall("jamuna")
# a.entry_hall("meghna")
jamuna = Hall(3, 4, 102)
jamuna.entry_show("S1", "Inception", "10am")
jamuna.entry_show("S2" , "Titanic" , "10pm")
jamuna.entry_show("S3" , "3 idots" , "7pm")
jamuna.entry_show("S4" , "persuit of happiness" , "4pm")


run = True
while run:
    option = int(input("Select an option \n 1: View shows\n 2: View available seats\n 3: Book tickets\n 4:Exit \n "))
    if option == 4:
        break
    else:
        Counter.select_option(option, jamuna)
