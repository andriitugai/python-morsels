# from datetime import date, datetime
import datetime
import fractions
import calendar

def is_over(age, birthdate):
    """
    returns if <age> years have passed since <date>. (For current time)
    :param age: int
    :param birthdate: str "YYYY-mm-dd"
    :return: boolean
    """
    full_years = get_age(birthdate)
    return age <= full_years

def get_age(birthdate, exact=False):
    """
    Return num of full years passed since <birthdate>
    :param birthdate: str "YYYY-mm-dd"
    :return:
    """
    today = datetime.datetime.today()
    # today = datetime.datetime.strptime("3000-02-28", "%Y-%m-%d")
    birthday = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
    bd_month = birthday.month
    bd_day = birthday.day
    if bd_day == 29 and bd_month == 2:
        bd_day = 1
        bd_month = 3
    this_year_bd = datetime.datetime(today.year, bd_month, bd_day)

    full_years = today.year - birthday.year
    if today < this_year_bd:
        full_years -= 1

    if not exact:
        return full_years

    delta = (today - this_year_bd).days
    days_in_year = 366 if calendar.isleap(today.year) else 365
    if delta > 0:
        frac = fractions.Fraction(delta, days_in_year)
    else:
        frac = fractions.Fraction(delta + days_in_year, days_in_year)

    return full_years + frac


def main():
    print(is_over(65, '1935-04-08'))
    print(is_over(16, '2984-02-29'))  # False
    print(is_over(16, '2984-02-27'))  # True
    print(is_over(16, '2984-03-01'))  # False

    print(get_age("1965-11-03", exact=True))


if __name__ == '__main__':
    main()

