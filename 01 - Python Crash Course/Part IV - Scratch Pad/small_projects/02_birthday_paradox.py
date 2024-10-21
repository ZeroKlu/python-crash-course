"""Birthday Paradox Simulation"""

import datetime
import random

MONTHS = [
    None, "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
MAX_SIMS = 100_000

def is_leap_year(year):
    """Check if a year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_birthdays(number_birthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for _ in range(number_birthdays):
        year = random.randint(1900, datetime.date.today().year)
        days = 365 if is_leap_year(year) else 364
        start_of_year = datetime.date(year, 1, 1)
        birthday = start_of_year + datetime.timedelta(random.randint(0, days))
        birthdays.append((birthday.month, birthday.day))
    return birthdays

def has_matches(birthdays):
    """Check if there are any duplicate dates in a list"""
    return len(birthdays) > len(set(birthdays))

def get_matches(birthdays):
    """Get all duplicate days in list"""
    if not has_matches(birthdays):
        return None
    matches = []
    # pylint: disable=consider-using-enumerate
    for i in range(len(birthdays)):
        dup = birthdays[:]
        day = birthdays[i]
        del dup[i]
        if day in dup and day not in matches:
            matches.append(day)
    return matches

def get_number_of_birthdays():
    """Get the number of people's birthdays to generate from the user"""
    num_bd = 0
    print("\nHow many birthdays should we generate? (1 to 100)")
    while num_bd == 0:
        resp = input("> ")
        if not resp.isdecimal() or int(resp) not in list(range(1, 100)):
            print("Please enter an integer between 1 and 100...")
            continue
        num_bd = int(resp)
    return num_bd

def single_simulation(num_bd):
    """Run a single simulation of the birthday paradox"""
    birthdays = get_birthdays(num_bd)
    matches = get_matches(birthdays)
    print("\nSingle Simulation")
    if has_matches(birthdays):
        print("Matches:\n----------")
        for m in matches:
            month, day = m
            suffix = "st" if day in [1, 21, 31] else ("nd" if day in [2, 22] \
                     else ("rd" if day in [3, 23] else "th"))
            print(f"{MONTHS[month]} {day}{suffix}")
    else: print("No matches found")
    input("\nPress <ENTER> to continue...")

def multiple_simulations(num_bd):
    """Run multiple (MAX_SIMS) simulations of the birthday paradox"""
    print(f"\nProcessing {MAX_SIMS:,} simulations...")
    matched_count = 0
    for i in range(MAX_SIMS):
        if i > 0 and i % 10_000 == 0:
            print(f"{i:,}", "simulations completed...")
        birthdays = get_birthdays(num_bd)
        matches = get_matches(birthdays)
        if matches:
            matched_count += 1
    print(f"{MAX_SIMS:,} simulations completed...")
    probability = round(matched_count / MAX_SIMS * 100, 2)
    print(f"\nOut of {MAX_SIMS:,} simulations of {num_bd} people, " + \
          "there was a matching birthday in that group {matched_count:,} times.")
    print(f"This means that {num_bd} people have a {probability}% chance" + \
          "of having a matching birthday in their group.")
    print("That's probably more than you would think!\n")

def main():
    """Main Program"""
    num_bd = get_number_of_birthdays()
    single_simulation(num_bd)
    multiple_simulations(num_bd)

if __name__ == "__main__":
    main()
