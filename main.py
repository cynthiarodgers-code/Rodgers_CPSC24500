"""
main.py - Week 4 Starter

Loads employees from employees.txt, then runs a menu loop.
"""

from payroll_processor import PayrollProcessor
from payroll_report import PayrollReport


def main():
    # TODO: create a PayrollProcessor
    # TODO: call load_from_file("employees.txt")
    # TODO: create a PayrollReport with the processor

    # TODO: loop showing a menu:
    #   1. View all employees
    #   2. View payroll summary
    #   3. Generate report file
    #   4. Quit
    
 def __init__(self, employee_id, name, hourly_rate):
        self.employee_id = employee_id
        self.name = name
        self.hourly_rate = float(hourly_rate)
        self.hours_worked = 0

def calculate_pay(self):
    """Calculates pay, including overtime (1.5x) for hours > 40."""
    if self.hours_worked <= 40:
        return self.hours_worked * self.hourly_rate
    else:
        regular_pay = 40 * self.hourly_rate
        overtime_pay = (self.hours_worked - 40) * (self.hourly_rate * 1.5)
        return regular_pay + overtime_pay



if __name__ == "__main__":
    main()
