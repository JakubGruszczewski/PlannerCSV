import pandas as pd


def additional_options():
    chosen_variant = input(
        "1. Ascending sort by date&time.\n"
        "2. Descending sort by date&time.\n"
        "3. Alphabetical order.\n"
        "4. Rever alphabetical order.\n"
        "5. Look for a keyword in name&description.\n"
        "6. Return.\n")
    chosen_variant = chosen_variant[0]

    if int(chosen_variant) == 1:
        df = pd.read_csv('Events.csv')
        df_sorted = df.sort_values(by=["Date", "Time"], ascending=True)
        print(df_sorted.to_string(index=False))

    elif int(chosen_variant) == 2:
        df = pd.read_csv('Events.csv')
        df_sorted = df.sort_values(by=["Date", "Time"], ascending=False)
        print(df_sorted.to_string(index=False))

    elif int(chosen_variant) == 3:
        df = pd.read_csv('Events.csv')
        sorted_alphabetically = df.sort_values("Name", ascending=True)
        print(sorted_alphabetically.to_string(index=False))

    elif int(chosen_variant) == 4:
        df = pd.read_csv('Events.csv')
        sorted_alphabetically = df.sort_values("Name", ascending=False)
        print(sorted_alphabetically.to_string(index=False))

    elif int(chosen_variant) == 5:
        keyword = input("Enter the search term: ")
        df = pd.read_csv('Events.csv')
        df_filtered = df[df["Name"].str.contains(keyword, case=False, na=False)
                         | df["Description"].str.contains(keyword, case=False, na=False)]
        if df_filtered.empty:
            print("No event has been found.")
        else:
            print(df_filtered.to_string(index=False))

    elif int(chosen_variant) == 6:
        print("Return.\n")
        return 1
    else:
        print("Incorrect input\n")
        additional_options()
