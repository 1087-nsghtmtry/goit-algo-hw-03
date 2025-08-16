from datetime import datetime, date

"""
функція, яка розраховує кількість днів між заданою датою і поточною датою.
Функція приймає один параметр: date (дату у форматі 'РРРР-ММ-ДД')
Функція повертає ціле число, 
яке вказує на кількість днів від заданої дати до поточної. 
Якщо задана дата пізніша за поточну, результат є від'ємним.
"""

def get_days_from_today(date):
    date_today = datetime.today().date()
    try:
        date_entered = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Wrong date format entered")
        return
    differ = (date_entered - date_today).days
    return differ

get_date = input(f"Please enter the date: ")
print(get_days_from_today(get_date))

