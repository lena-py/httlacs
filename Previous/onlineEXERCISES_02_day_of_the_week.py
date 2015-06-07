# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday.
# Ask for the starting day number, and the length of your stay,
# and return the number of day of the week you will return on.

# modified original code to incorporate new knowledge
import string


def reverse_dict(dct):
    """
    Create a new dictionary swapping the old dictionary's keys for values and vice versa
    :param dct: Old dictionary
    :return: New dictionary
    """
    dict_rvrs = {}
    dict_items = list(dct.items())
    for i in dict_items:
        dict_rvrs[i[1]] = i[0]
    return dict_rvrs


def data_vldt(vlu, lkup, msg):
    """
    Validate user entry against a set of values
    :param vlu: User entry
    :param lkup: Data against which to validate vlu
    :param msg: Message to user for invalid entry
    :return: Original value
    """
    if type(lkup) == dict:
        while vlu not in lkup:
            vlu = input(msg)
    else:
        count = 0
        while count < len(vlu):
            for i in vlu:
                if i not in lkup:
                    vlu = input(msg)
                    count = 0
                else:
                    count += 1

    return vlu


def main():
    days = {0: "sunday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday", 1: "monday"}
    reverse_days = reverse_dict(days)
    current_day = input("Enter the current day\n").lower()
    current_day = data_vldt(current_day, reverse_days, "Not a valid day.\n")
    vacation_days = input("Enter the number of vacation days \n")
    vacation_days = int(data_vldt(vacation_days, string.digits, "Not a valid number.\n"))

    crnt_day_int = reverse_days.get(current_day)
    return_day_int = (crnt_day_int + vacation_days) % 7
    return_day_str = days.get(return_day_int)

    print("You will return on a", return_day_str[0:1].upper()+return_day_str[1:])

if __name__ == "__main__":
    main()






