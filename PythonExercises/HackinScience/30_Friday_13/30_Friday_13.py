from datetime import date, timedelta

def friday_the_13th():
    from_date = date.today()
    d = from_date + timedelta(13 - from_date.day)

    def increment_month(d):
        month = 1 if d.month == 12 else d.month + 1
        year = d.year + 1 if month == 1 else d.year
        return date(year, month, d.day)

    if from_date > d:
        increment_month(d)

    while True:
        if d.weekday() == 4:
            return d
        d = increment_month(d)

print(friday_the_13th())