from datetime import datetime
import csv


def add_event():
    print("New event data")

    date = input("Date (YYYY-MM-DD):")
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return "date"

    time = input("Time (HH:MM):")
    try:
        datetime.strptime(time, '%H:%M')
    except ValueError:
        return "time"

    name = input("Name:")
    if name == "":
        return "name"
    try:
        name.capitalize()
    except ValueError:
        pass
    name = name.capitalize()

    description = input("Event description:")

    with open('Events.csv', 'a', newline='') as events:
        writer = csv.writer(events)
        writer.writerow([date, time, name, description])
