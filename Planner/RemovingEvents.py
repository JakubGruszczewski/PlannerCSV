import pandas as pd


def remove_event(date, time, name):

    df = pd.read_csv('Events.csv')
    r_line = df[(df.Data == date) & (df.Godzina == time) & (df.Nazwa == name)]
    if r_line.empty:
        result = "No event has been found, therefore no event has been removed."
    else:
        result = "Event has been removed."
        df = df.drop(r_line.index)
    df.to_csv('Events.csv', index=False)
    return result
