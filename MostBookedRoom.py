'''We have to find the most booked hotel room  and return in the smallest lexicrographical hotel'''

from collections import Counter


def max_booking(booking):
    booked_times = {}
    for room in booking:
        if room[0] == '+':
            booked_times[room[1:]] = booked_times.get(room[1:], 0) + 1

    most_booked = sorted(booked_times.items(), key=lambda x: (-x[1], x[0]))

    return most_booked[0][0]

input=["+9A", "+3E", "+4F", "+6A", "+8E","-9A", "-3E", "-4F", "-6A", "-8E"]
print(max_booking(input))