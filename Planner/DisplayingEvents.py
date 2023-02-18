import csv


def display_events():
    with open('Events.csv', 'r') as events:
        events_reader = csv.reader(events, delimiter=',')
        next(events_reader)
        data = [row for row in events_reader]

    name_max_length = max([len(row[2]) for row in data])
    alpha = int(round(name_max_length/8)+1)
    for row in data:
        print(row[0], "\t", row[1], "\t", row[2], "\t" * alpha, row[3])
