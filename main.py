from datetime import datetime


def string_to_date(date_string):
   converted_date = datetime.strptime(date_string, "%Y.%m.%d").date()
   return converted_date
   


def date_to_string(date):
    converted_string = datetime.strftime(date, "%Y.%m.%d")
    return converted_string


date_string = "2024.01.01"
converted_date = string_to_date(date_string)
print(converted_date)
date = string_to_date
date_string = date_to_string(converted_date)
print(date_string)