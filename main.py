from application.db import people
from application import salary
from datetime import datetime, date, time

if __name__ == '__main__':
    print('Текущая дата и время:\n', datetime.now())
    print()
    people.get_employees()
    salary.calculate_salary()
