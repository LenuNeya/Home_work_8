from datetime import date, timedelta
from collections import defaultdict


TODAY = date.today()
END_WEEK = TODAY + timedelta(days=7)


def get_birthdays_per_week(employees):
    
    grouped_birthdays = defaultdict(list)
    for employee in employees:
        birthday = employee['birthday']
        next_birthday = get_next_birthday(birthday, TODAY.year)

        if TODAY < next_birthday <= END_WEEK:
            week_day = next_birthday.weekday()
            if week_day > 4:
                grouped_birthdays['Monday'].append(employee['name'])
            else:
                grouped_birthdays[next_birthday.strftime('%A')].append(employee['name'])
    
    for day, persons in grouped_birthdays.items():
        print('{:<9}: {:<10}'.format(day, ', '.join(persons)))
        

def get_next_birthday(birthday, year):
    
    try:
        next_birthday = birthday.replace(year=year)
    except ValueError:
        next_birthday = birthday.replace(year=year, month=birthday.month+1, day=1)
    
    if next_birthday < TODAY:
        return get_next_birthday(next_birthday, year + 1, TODAY)
    else:
        return next_birthday


if __name__ == '__main__':
    
    employees = [
        {
        'name': 'John',
        'birthday': date(year=2000, month=11, day=5)
        },
        {
        'name': 'Bill',
        'birthday': date(year=2000, month=11, day=6)
        },
        {
        'name': 'Jill',
        'birthday': date(year=2000, month=11, day=7)
        },
        {
        'name': 'Jan',
        'birthday': date(year=2000, month=11, day=10)
        },
        {
        'name': 'Kim',
        'birthday': date(year=2000, month=11, day=10)
        }
    ]
    get_birthdays_per_week(employees)
    