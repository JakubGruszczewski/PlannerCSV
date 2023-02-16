from AddingEvents import add_event
from RemovingEvents import remove_event
from Operations import additional_options

#todo list
# 1. cofanie do menu po wykonaniu zadania
# 2. lepsze wyswietlanie
# 3. dodanie GUI


def main_menu():
    chosen_variant = input(
        "   \U0001F4C5 Planner \U0001F4C5 \n "
        "   Choose option:\n"
        "       1.[\U0001F4BB] Display event(s)\n"
        "       2.[\U00002795] Add event\n"
        "       3.[\U0000274C] Remove event\n"
        "       4.[\U0001F527] Additional options\n"
        "       5.[\U000021B3] Exit\n"
    )

    if chosen_variant != "" and 49 <= ord(chosen_variant[0]) <= 52:
        pass
    else:
        print("Incorrect input")
        main_menu()

    if int(chosen_variant) == 1:
        with open("Events.csv") as events:
            print(events.read())

    elif int(chosen_variant) == 2:
        error = add_event()
        if error is not None:
            print(f"Incorrect {error} input.")
            main_menu()
        else:
            print("Event added.")

    elif int(chosen_variant) == 3:
        print("Removed event data:")
        r_date = input("Date (YYYY-MM-DD): ")
        r_time = input("Time (HH:MM): ")
        r_name = input("Name: ")
        print(remove_event(r_date, r_time, r_name))

    elif int(chosen_variant) == 4:
        options = additional_options()
        if options == 1:
            main_menu()

    elif int(chosen_variant) == 5:
        exit(print("Program has been terminated"))


main_menu()
