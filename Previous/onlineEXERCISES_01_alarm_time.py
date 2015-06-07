__author__ = 'lena'
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on the clock when the alarm goes off. (1
import string


def data_vld(vlu, lkup, msg):
    """
    Check that the value is contained in the lookup values.
    Will check against a list or iterate through a string
    :param vlu: the value to be validated
    :param lkup: the list or collection against which to validate value
    :param msg: the message displayed for an invalid entry
    :return: original value
    """
    if type(lkup) == list:
        count = False
        while count is False:
            try:
                vlu = int(vlu)
                if vlu not in lkup:
                    vlu = input(msg)
                else:
                    count = True
            except Exception:
                vlu = input(msg)
                # vlu = input(msg)
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


def alarm(time, alrm):
    """
    The time an alarm will go off
    :param time: current time
    :param alrm: number of hours until the alarm
    :return: hour the alarm will ring
    """
    return (time + alrm) % 24


def main():
    clock_hrs = list(range(25))

    time_now = input("Enter the current hour\n")
    time_now = int(data_vld(time_now, clock_hrs, "not a valid hour\n"))
    no_of_hours = input("Enter the number of hours to wait for the alarm\n")
    no_of_hours = int(data_vld(no_of_hours, string.digits, "not a valid number of hours\n"))

    print("The alarm will go off at", alarm(time_now, no_of_hours))

if __name__ == "__main__":
    main()

