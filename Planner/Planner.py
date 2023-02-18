from DisplayingEvents import display_events
from AddingEvents import add_event
from RemovingEvents import remove_event
from Operations import additional_options


def return_function():
    return_input = input("Press any key to return to main menu.\n")
    if return_input is not None:
        main_menu()


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

    if chosen_variant != "" and 49 <= ord(chosen_variant[0]) <= 53:
        pass
    else:
        print("Incorrect input")
        main_menu()

    if int(chosen_variant) == 1:
        display_events()
        return_function()

    elif int(chosen_variant) == 2:
        error = add_event()
        if error is not None:
            print(f"Incorrect {error} input.")
            main_menu()
        else:
            print("Event added.")
            return_function()

    elif int(chosen_variant) == 3:
        print("Removed event data:")
        r_date = input("Date (YYYY-MM-DD): ")
        r_time = input("Time (HH:MM): ")
        r_name = input("Name: ")
        print(remove_event(r_date, r_time, r_name))
        return_function()

    elif int(chosen_variant) == 4:
        options = additional_options()
        if options == 1:
            main_menu()
        return_function()

    elif int(chosen_variant) == 5:
        exit(print("Program has been terminated"))


main_menu()
