import datetime


class Time:
    """ Represents the time of the day 

    attrtibutes : hour, minute, second
    """


def print_time(T):
    """ Print time in HH:MM:SS format """
    print(("{:02d}:{:02d}:{:02d}").format(T.hour, T.minute, T.second))


def is_after(t1, t2):
    """ Check if t2 > t1 where t1 and t2 are Time objects """
    total_seconds_1 = time_to_seconds(t1)
    total_seconds_2 = time_to_seconds(t2)
    return total_seconds_2 > total_seconds_1


def seconds_to_time(seconds):
    """ Convert total seconds to hours, minutes <= 60, seconds <= 60 """
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds


def time_to_seconds(time):
    """ Convert hours, minutes and seconds to total seconds """
    return time.second + time.minute * 60 + time.hour * 3600


def increment(time, seconds):
    """
    increment time object with total seconds
    """
    new_seconds = seconds + time_to_seconds(time)
    time.hour, time.minute, time.second = seconds_to_time(new_seconds)


def pure_increment(time, seconds):
    """
    Retruns a new time object incremented with total seconds
    """
    new_time = Time()
    new_seconds = seconds + time_to_seconds(time)
    new_time.hour, new_time.minute, new_time.second = seconds_to_time(new_seconds)
    return new_time


def add_times(t1, t2):
    """ add two time objects and return the result as a new time object """
    new_time = Time()
    new_seconds = time_to_seconds(t1) + time_to_seconds(t2)
    new_time.hour, new_time.minute, new_time.second = seconds_to_time(new_seconds)
    return new_time


def valid_time(time):
    """ Check if time is a valid Time object """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.hour >= 60:
        return False
    return True


def mul_time(time, num):
    """ Product of time and number """
    assert valid_time(time)
    return seconds_to_time(time_to_seconds(time) * num)


def time_per_mile(time, distance):
    """ return average pace (time per mile) """
    return mul_time(time, 1 / distance)


def get_birthday():
    #    year = int(input("Input Birthday Year as int "))
    #    month = int(input("Input Birthday month as int "))
    #    day = int(input("Input Birthday day as int "))
    year = 1995
    month = 6
    day = 18
    x = datetime.datetime(year, month, day)
    return x


def coming_birthday(birthday):
    """ Given actual birthday return date of next comming birthday """
    current_date = datetime.datetime.today()
    cbirthday = datetime.datetime(
        year=current_date.year, month=birthday.month, day=birthday.day
    )
    if cbirthday > current_date:
        return cbirthday
    nbirthday = datetime.datetime(
        year=current_date.year + 1, month=birthday.month, day=birthday.day
    )
    return nbirthday


def calculate_age(birthday):
    current_date = datetime.datetime.today()
    age = current_date - birthday
    return age


if __name__ == "__main__":
    time = Time()
    time.hour = 2
    time.minute = 3
    time.second = 22
    print_time(time)
    current_date = datetime.datetime.today()
    birthday = get_birthday()
    next_birthday = coming_birthday(birthday)
    print("till next birthday : ", next_birthday - current_date)
    print(calculate_age(birthday) + current_date)

