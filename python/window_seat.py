no_of_seats=int(input('Enter the number of seats per row\n'))
total_seats=11*no_of_seats
if no_of_seats<=0:
    print('Invalid input')
    quit()
else:
    seat_number=int(input('Enter the seat number\n'))
    if seat_number<=0 or seat_number>total_seats:
        print('Invalid seat number')
        quit()
    else:
        if seat_number%no_of_seats==0:
            print('Window Seat')
        else:
            print('Not a Window Seat')