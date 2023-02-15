from application.salary import calculate_salary
from application.db.people import get_employess

if __name__ == '__main__':
    get_employess()
    calculate_salary()