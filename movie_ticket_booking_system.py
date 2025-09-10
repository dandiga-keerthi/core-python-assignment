def show_available(total, booked):
    return [s for s in range(1, total+1) if s not in booked]

def book_seat(booked, seat, total):
    if seat not in booked and 1 <= seat <= total:
        booked.append(seat)
    return booked

def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
    return booked

total_seats = int(input("Enter total number of seats: "))
booked_seats = list(map(int, input("Enter booked seats (space separated): ").split()))
book_seat_num = int(input("Enter seat number to book: "))
cancel_seat_num = int(input("Enter seat number to cancel: "))

booked_seats = book_seat(booked_seats, book_seat_num, total_seats)
booked_seats = cancel_seat(booked_seats, cancel_seat_num)
print("Available seats:", show_available(total_seats, booked_seats))
