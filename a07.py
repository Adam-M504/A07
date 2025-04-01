import pandas as pd

# Create the database
data = {
    'Year': [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022],
    'Winner': ['Uruguay', 'Italy', 'Italy', 'Uruguay', 'Germany', 'Brazil', 'Brazil', 'England', 'Brazil', 'Germany', 'Argentina', 'Italy', 'Argentina', 'Germany', 'Brazil', 'France', 'Brazil', 'Italy', 'Spain', 'Germany', 'France', 'Argentina'],
    'Runner-up': ['Argentina', 'Czechoslovakia', 'Hungary', 'Brazil', 'Hungary', 'Sweeden', 'Czechoslovakia', 'Germany', 'Italy', 'Netherlands', 'Netherlands', 'Germany', 'Germany', 'Argentina', 'Italy', 'Brazil', 'Germany', 'France', 'Netherlands', 'Argentina', 'Croatia', 'France']
}
results = pd.DataFrame(data)

while True:
    inp = input("-Type 'view' to view all countries that have won the world cup\n"
    "-Type 'spec' to look at the wins for a specific country\n"
    "-Type 'year' to look at the top teams for a specific year\n"
    "-Type 'quit' to exit.\n"
    "Your Command: ").lower()

    if inp == "view":
        print("Here are all the Countries that have won a world cup:\n")
        print(results['Winner'].unique(), '\n')
    elif inp == "spec":
        country = input("Please enter the country you want stats on: ").capitalize()
        win_results = results[results['Winner'] == country]
        if win_results.empty:
            print(f"\n{country} is yet to win a world cup.\n")
        else:
            print(f"\n{country} has won the world cup {len(win_results)} time(s).\n")

    elif inp == "year":
        try:
            year_inp = int(input("Enter the year you want the information on: "))
        except ValueError:
            print("You did not enter a valid date.")
            continue

        year_results = results[results['Year'] == year_inp]
        if not year_results.empty:
            print(f"\nThe winner in {year_inp} was {year_results.iloc[0]['Winner']} and the runner up was {year_results.iloc[0]['Runner-up']}.\n")
        else:
            print("There was no world cup in that year.")

    elif inp == 'quit' or inp == "q" or inp == "exit":
        break
