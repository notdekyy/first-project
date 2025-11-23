from dataclasses import dataclass
maxseats=50
maxnamelength=50

# Class to store boooking details
class Booking:
    def __init__(self):
        self.name=""
        self.age=0
        self.source=""
        self.destination=""
        self.seatnumber=0
        self.isbooked= False

train = [Booking() for i in range(maxseats)] # List to store booking details

# Intialize the train seats as displayAvailableSeats
def initializeSeats():
    for j in range(maxseats):
        # False represents available seats
        train[j].isbooked= False

# Function to display maxseats
def displayAvailableSeats():
    print("Available Seats:")
    for z in range(maxseats):
        if not train[z].isbooked:
            print(f"Seat {z+1}")

# Function to display booked seats
def displayBookedSeats():
    print("--- Booked Seats & Passengers ---")
    booked_count = 0
    
    # Iterate through all seats
    for i in range(maxseats):
        if train[i].isbooked:
            print(f"Seat {train[i].seatnumber:2d}: {train[i].name} (Age: {train[i].age}) - Route: {train[i].source} to {train[i].destination}")
            bookedcount += 1
            
    if bookedcount == 0:
        print("No seats are currently booked.")
    print("---------------------------------")


# Function to book seats
def bookSeat():
    seatnumber = int(input("Enter Seat Number to Book: ")) - 1 # Adjust Index

    if seatnumber < 0 or seatnumber >= maxseats:
        print("Invalid Seat Number")
        return
    
    if train[seatnumber].isbooked:
        print("Seat is Already Booked")
    else:
        train[seatnumber].isbooked = True
        # Actual Seat Number
        train[seatnumber].seatnumber = seatnumber + 1
        train[seatnumber].name = input("Enter Passenger Name: ").strip()
        train[seatnumber].age = int(input("Enter Passenger Age: "))
        train[seatnumber].source = input("Enter Source: ").strip()
        train[seatnumber].destination = input("Enter Destination: ").strip()    
        print("Seat Booked Successfully!")

# Function to cancel a seat booking 
def cancelSeat():
    # Adjust Index
    seatnumber = int(input("Enter Seat Number to Cancel your Booking: ")) - 1

    if seatnumber < 0 or seatnumber >= maxseats:
        print("Invalid Seat Number")
        return
    
    if train[seatnumber].isbooked:
        train[seatnumber].isbooked = False
        print("Seat Booking Cancelled Successfully")
    else:
        print("Seat is not Booked")

# Function to Print Ticket Details
def printTicket(seatnumber):
    # Adjust Index

    seatnumber -= 1

    if seatnumber<0 or seatnumber >= maxseats:
        print("Invalid Seat Number")
        return
    
    if train[seatnumber].isbooked:
        print("Ticket Details:")
        print(f"Name: {train[seatnumber].name}")
        print(f"Age: {train[seatnumber].age}" )
        print(f"Source: {train[seatnumber].source}")
        print(f"Destination: {train[seatnumber].destination}")
        print(f"Seat Number: {train[seatnumber].seatnumber}")
    else:
        print("Seat is not Booked")


    



def main():
    initializeSeats()
    choice = 0
    while choice !=6:
        print("Train Booking System")
        print("1. Display Available Seats")
        print("2. Book a Seat")
        print("3. Display Booked Seats")
        print("4. Cancel a Seat Booking")
        print("5. Print Ticket")
        print("6. Exit")
        choice=int(input("Enter Your Choice: "))

        if choice ==1:
            displayAvailableSeats()
        elif choice ==2:
            bookSeat()
        elif choice==3:
            displayBookedSeats()
        elif choice==4:
            cancelSeat()
        elif choice == 5:
            seatnumber=int(input("Enter Seat Number to Print Ticket: "))
            printTicket(seatnumber)
        elif choice==6:
            print("Exiting...")
        else:
            print("Invalid Choice")

if __name__=="__main__":
    main()


 


