from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
        today_date = datetime.today()
        days_from_today = (today_date - input_date).days
        return (print(days_from_today))
    except ValueError:
        return (print("Date format must be 'YYYY-MM-DD'"))
    except TypeError:
        return (print("Date format must containe only digits and be in 'YYYY-MM-DD' format"))

get_days_from_today("2020-10-09")