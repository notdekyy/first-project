# Train Booking System - CSE Project

**VIT Bhopal University**  
**Course:** Computer Science and Engineering  
**Submitted To:** Professor Sasmita Padhy  
**Student Name:** Chirag Bhatia  
**Registration Number:** 25BAI10766  
**Date of Submission:** November 23, 2025

---

## Overview

The **Train Booking System** is a console-based application developed in Python that simulates a railway reservation management system. This project demonstrates fundamental concepts of data structures, object-oriented programming, and user-interactive applications. The system allows users to book train seats, view available and booked seats, cancel bookings, and print ticket details.

---

## Project Objectives

- Implement a practical railway seat management system using Python
- Demonstrate proficiency in **object-oriented programming (OOP)** concepts
- Utilize **data structures** such as lists and classes for efficient data storage
- Create an **interactive menu-driven interface** for user engagement
- Implement **validation mechanisms** to ensure data integrity
- Practice **modular programming** with well-defined functions
- Apply **algorithmic thinking** for business logic implementation

---

## Features

### 1. **Initialize Train Seats**
- Sets up 50 available seats in the train
- All seats are initially marked as unbooked

### 2. **Display Available Seats**
- Shows all unbooked seats in the train
- Helps passengers identify available seating options

### 3. **Book a Seat**
- Allows passengers to reserve a seat
- Collects passenger information: name, age, source, and destination
- Validates seat availability before booking
- Provides confirmation upon successful booking

### 4. **Display Booked Seats**
- Shows all reserved seats with passenger details
- Displays seat number, passenger name, age, and route information
- Provides a comprehensive view of current bookings

### 5. **Cancel a Seat Booking**
- Enables passengers to cancel their reservations
- Validates seat status before cancellation
- Provides confirmation upon successful cancellation

### 6. **Print Ticket**
- Generates ticket details for a booked seat
- Displays passenger information and journey route
- Validates seat booking status before printing

---

## Technical Stack

| Component | Details |
|-----------|---------|
| **Programming Language** | Python 3.x |
| **Data Structure** | Classes, Lists |
| **Programming Paradigm** | Object-Oriented Programming (OOP) |
| **User Interface** | Console-Based Menu System |
| **Total Seats** | 50 |
| **Maximum Name Length** | 50 characters |

---

## System Architecture

### Class Structure

**Booking Class:**
```
Attributes:
- name: str (Passenger's full name)
- age: int (Passenger's age)
- source: str (Journey starting point)
- destination: str (Journey ending point)
- seatnumber: int (Assigned seat number)
- isbooked: bool (Booking status - True if booked, False if available)
```

### Data Storage
- **train[]**: A list containing 50 Booking objects representing each seat in the train

---

## How to Run

### Prerequisites
- Python 3.x installed on your system
- Basic familiarity with command-line interface

### Execution Steps

1. **Navigate to the project directory** in terminal/command prompt
   ```bash
   cd path/to/project
   ```

2. **Run the Python script**
   ```bash
   python train-ticket-system.py
   ```

3. **Follow the on-screen menu** to perform desired operations:
   - Enter `1` to view available seats
   - Enter `2` to book a seat
   - Enter `3` to view booked seats
   - Enter `4` to cancel a booking
   - Enter `5` to print a ticket
   - Enter `6` to exit

---

## Screenshots

### Screenshot 1: Main Menu Interface
![Main Menu](2.jpg)
The main menu presents all available operations with a clear, numbered choice system.

### Screenshot 2: Code Implementation
![Code Implementation](1.jpg)
Shows the core Python implementation including class definition and function declarations.

### Screenshot 3: Program Output Example
![Program Output](3.jpg)
Demonstrates the system's output format and user interaction flow.

---

## Pseudocode

### Initialize Seats Function
```
ALGORITHM initializeSeats()
    FOR j = 0 TO maxseats - 1 DO
        train[j].isbooked ← FALSE
    END FOR
END ALGORITHM
```

### Display Available Seats Function
```
ALGORITHM displayAvailableSeats()
    PRINT "Available Seats:"
    FOR z = 0 TO maxseats - 1 DO
        IF train[z].isbooked == FALSE THEN
            PRINT "Seat ", z + 1
        END IF
    END FOR
END ALGORITHM
```

### Book Seat Function
```
ALGORITHM bookSeat()
    INPUT seatnumber
    seatnumber ← seatnumber - 1  // Adjust for 0-based indexing
    
    IF seatnumber < 0 OR seatnumber >= maxseats THEN
        PRINT "Invalid Seat Number"
        RETURN
    END IF
    
    IF train[seatnumber].isbooked == TRUE THEN
        PRINT "Seat is Already Booked"
    ELSE
        train[seatnumber].isbooked ← TRUE
        train[seatnumber].seatnumber ← seatnumber + 1
        INPUT train[seatnumber].name
        INPUT train[seatnumber].age
        INPUT train[seatnumber].source
        INPUT train[seatnumber].destination
        PRINT "Seat Booked Successfully!"
    END IF
END ALGORITHM
```

### Display Booked Seats Function
```
ALGORITHM displayBookedSeats()
    PRINT "--- Booked Seats & Passengers ---"
    booked_count ← 0
    
    FOR i = 0 TO maxseats - 1 DO
        IF train[i].isbooked == TRUE THEN
            PRINT Seat Details: Seat Number, Name, Age, Route
            booked_count ← booked_count + 1
        END IF
    END FOR
    
    IF booked_count == 0 THEN
        PRINT "No seats are currently booked."
    END IF
    
    PRINT "---------------------------------"
END ALGORITHM
```

### Cancel Seat Function
```
ALGORITHM cancelSeat()
    INPUT seatnumber
    seatnumber ← seatnumber - 1  // Adjust for 0-based indexing
    
    IF seatnumber < 0 OR seatnumber >= maxseats THEN
        PRINT "Invalid Seat Number"
        RETURN
    END IF
    
    IF train[seatnumber].isbooked == TRUE THEN
        train[seatnumber].isbooked ← FALSE
        PRINT "Seat Booking Cancelled Successfully"
    ELSE
        PRINT "Seat is not Booked"
    END IF
END ALGORITHM
```

### Print Ticket Function
```
ALGORITHM printTicket(seatnumber)
    seatnumber ← seatnumber - 1  // Adjust for 0-based indexing
    
    IF seatnumber < 0 OR seatnumber >= maxseats THEN
        PRINT "Invalid Seat Number"
        RETURN
    END IF
    
    IF train[seatnumber].isbooked == TRUE THEN
        PRINT "Ticket Details:"
        PRINT train[seatnumber].name
        PRINT train[seatnumber].age
        PRINT train[seatnumber].source
        PRINT train[seatnumber].destination
        PRINT train[seatnumber].seatnumber
    ELSE
        PRINT "Seat is not Booked"
    END IF
END ALGORITHM
```

### Main Function
```
ALGORITHM main()
    initializeSeats()
    choice ← 0
    
    WHILE choice ≠ 6 DO
        PRINT Main Menu Options
        INPUT choice
        
        SWITCH choice
            CASE 1:
                displayAvailableSeats()
            CASE 2:
                bookSeat()
            CASE 3:
                displayBookedSeats()
            CASE 4:
                cancelSeat()
            CASE 5:
                INPUT seatnumber
                printTicket(seatnumber)
            CASE 6:
                PRINT "Exiting..."
            DEFAULT:
                PRINT "Invalid Choice"
        END SWITCH
    END WHILE
END ALGORITHM
```

---

## System Workflow

### Main Application Flow
```
START
    ↓
Initialize Train Seats (all seats marked as available)
    ↓
Display Main Menu
    ↓
User Makes Selection
    ├─→ Option 1: View Available Seats → Display List → Return to Menu
    ├─→ Option 2: Book Seat → Input Details → Validate → Confirm → Return to Menu
    ├─→ Option 3: View Booked Seats → Display List → Return to Menu
    ├─→ Option 4: Cancel Booking → Input Seat → Validate → Confirm → Return to Menu
    ├─→ Option 5: Print Ticket → Input Seat Number → Validate → Display Details → Return to Menu
    └─→ Option 6: Exit → END
    ↓
Loop Until User Chooses Exit
```

---

## Flowchart

```
                        ┌─────────────────────┐
                        │      START          │
                        └──────────┬──────────┘
                                   │
                        ┌──────────▼──────────┐
                        │ Initialize Seats    │
                        │ (All = Available)   │
                        └──────────┬──────────┘
                                   │
                        ┌──────────▼──────────┐
                        │   Display Menu      │
                        └──────────┬──────────┘
                                   │
                ┌──────────────────┼──────────────────┐
                │                  │                  │
           ┌────▼─────┐      ┌─────▼────┐      ┌─────▼────┐
           │ Option 1  │      │ Option 2 │      │ Option 3 │
           │  Display  │      │  Book    │      │ Display  │
           │ Available │      │  Seat    │      │ Booked   │
           │  Seats    │      │          │      │  Seats   │
           └────┬─────┘      └─────┬────┘      └─────┬────┘
                │                  │                  │
           ┌────▼────┐         ┌────▼───────────┐    │
           │Show List│         │Valid Input?    │    │
           └────┬────┘         └┬──────────┬────┘    │
                │               │          │        │
                │               Y          N        │
                │               │          │        │
           ┌────▼──────┐   ┌────▼────┐ ┌──▼────┐   │
           │Return Menu│   │Book Seat│ │Error  │   │
           └───────────┘   └────┬────┘ └───┬───┘   │
                                │          │       │
                           ┌────▼──────┐   │       │
                           │Collect    │   │       │
                           │Details    │   │       │
                           └────┬──────┘   │       │
                                │          │       │
                           ┌────▼──────┬───▼───┐   │
                           │Confirm &  │Return │   │
                           │Update     │Menu   │   │
                           └────┬──────┴───┬───┘   │
                                │          │       │
                           ┌────▼──────────▼───┐   │
                           │   Return to Menu   │◄──┘
                           └────┬──────────────┘
                                │
                    ┌───────────┼───────────┐
                    │           │           │
                ┌───▼───┐   ┌───▼───┐  ┌───▼───┐
                │Option │   │Option │  │Option │
                │ 4, 5  │   │  6    │  │ 1-5   │
                │Cancel/│   │ Exit  │  │Repeat │
                │Print  │   │       │  │       │
                └───┬───┘   └───┬───┘  └───┬───┘
                    │           │          │
                ┌───▼───────────▼──────────▼───┐
                │  Return to Menu / Continue   │
                └───┬──────────────────────────┘
                    │
        ┌──────────┐ │
        │          │ │
        └──────────┘ │
                     │
             ┌───────▼────────┐
             │   Process Exit  │
             │    or Loop      │
             └───────┬────────┘
                     │
             ┌───────▼────────┐
             │      END       │
             └────────────────┘
```

---

## Key Data Structures Used

### 1. **Booking Class**
- Encapsulates all information for a single train seat reservation
- Implements OOP principles through data encapsulation

### 2. **List (Array) of Booking Objects**
- `train[]` stores 50 Booking instances
- Each index represents a physical seat in the train
- Provides O(1) access time for seat information

---

## Functions Overview

| Function | Purpose | Parameters | Return Type |
|----------|---------|-----------|-------------|
| `initializeSeats()` | Initialize all seats as available | None | None |
| `displayAvailableSeats()` | Show all vacant seats | None | None |
| `displayBookedSeats()` | Show all reserved seats with details | None | None |
| `bookSeat()` | Reserve a seat with passenger info | None | None |
| `cancelSeat()` | Cancel an existing booking | None | None |
| `printTicket(seatnumber)` | Display ticket for booked seat | int | None |
| `main()` | Main application loop | None | None |

---

## Data Flow

```
User Input
    ↓
Input Validation
    ↓
Data Processing
    ↓
Database Operation (List Update)
    ↓
Status Confirmation
    ↓
Display Result
    ↓
Return to Main Menu
```

---

## Error Handling

The system implements robust error handling for:

- **Invalid Seat Numbers**: Out of range seat selections are rejected
- **Duplicate Bookings**: Prevents booking of already reserved seats
- **Cancellation of Empty Seats**: Notifies user if trying to cancel non-existent booking
- **Invalid Menu Choices**: Prompts user to select valid options
- **Input Validation**: Ensures valid seat number range (1-50)

---

## Advantages of This Implementation

- **Simple and Intuitive**: Easy to understand for users and developers
- **Efficient Data Access**: List-based storage provides O(1) lookup time
- **Scalable**: Can easily expand to support more seats by changing `maxseats` constant
- **Modular Design**: Each function performs a specific task independently
- **Interactive Interface**: User-friendly menu-driven console application

---

## Limitations and Future Enhancements

### Current Limitations
- **No Persistence**: Data is lost when application terminates
- **Single Train**: System manages only one train
- **Limited Fields**: Basic passenger information only
- **No Database Integration**: Uses in-memory storage only

### Suggested Enhancements
- Add **file-based persistence** using CSV or JSON
- Implement **database integration** with SQLite or MySQL
- Add **multiple train support** with different routes
- Include **payment processing** and booking confirmation
- Add **user authentication** and booking history
- Implement **email notifications** for bookings
- Add **date-based scheduling** for different travel dates
- Include **pricing tiers** based on seat category
- Add **search functionality** for routes and timings
- Implement **cancellation policies** and refund calculation

---

## Testing Recommendations

### Test Cases

1. **Seat Availability Display**
   - Verify all 50 seats are initially displayed as available

2. **Booking Functionality**
   - Book a valid seat and verify status change
   - Attempt to book an already booked seat (should fail)
   - Test boundary conditions (Seat 1 and Seat 50)

3. **Cancellation**
   - Cancel a booked seat and verify availability
   - Attempt to cancel an unbooked seat (should fail)

4. **Ticket Printing**
   - Print ticket for booked seat and verify details
   - Attempt to print ticket for unbooked seat (should fail)

5. **Input Validation**
   - Test with invalid seat numbers (negative, > 50, non-numeric)
   - Test with empty passenger names
   - Test with invalid age values

---

## Conclusion

The Train Booking System project successfully demonstrates core concepts of Python programming including object-oriented design, data structure utilization, and interactive application development. This system serves as a foundation for understanding real-world ticketing systems and can be extended with additional features for practical deployment.

---

## References

- Python Official Documentation: https://docs.python.org/3/
- Object-Oriented Programming Principles
- Data Structures and Algorithms Fundamentals
- Software Engineering Best Practices

---

**Project Submitted:** November 23, 2025  
**Academic Year:** 2025-2026  
**Semester:** Fall
