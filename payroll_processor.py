"""
payroll_processor.py - Week 4 Starter

The PayrollProcessor manages a list of Employee objects and computes statistics.

Notes:
- self._employees should be private
- The `employees` property returns a COPY of the internal list (use list(self._employees))
- load_from_file() reads tab-delimited lines: name<TAB>id<TAB>rate<TAB>hours
- Skip blank lines and lines with the wrong number of fields (print a warning)
- Catch ValueError from the Employee constructor and print a warning
- Catch FileNotFoundError if the file doesn't exist
"""

from employee import Employee


class PayrollProcessor:

    def __init__(self):
        # TODO: initialize self._employees as an empty list
        self_employees = []
        

    @property
    def employees(self):
        # TODO: return a COPY of the list, not the original
        employee_copy = self_employees.copy()
        

    def load_from_file(self, filename):
        # TODO: open the file in a try/except for FileNotFoundError
        # TODO: for each line:
        #   - strip whitespace; skip blank lines
        #   - split on tab; if not exactly 4 fields, print a warning and continue
        #   - try to create an Employee; catch ValueError and print a warning
        #   - append to self._employees on success

        try:
            with open(filename, 'employee_copy') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    fields = line.split('\t')
                    if len(fields) != 4:
                        print(f"Warning: Skipping invalid line: {line}")
                        continue

                    try:
                        new_employee = Employee(*fields)
                    
                    except ValueError as e:
                        print(f"Warning: Could not create employee from line '{line}': {e}")
        except FileNotFoundError:
            print(f"Error: The file '{employee_copy}' was not found.")
        

    def calculate_total_payroll(self):
        # TODO: return the sum of gross pay across all employees
        return sum(employee.gross_pay for employee in self.employees)

    def find_highest_paid(self):
        # TODO: return the Employee with the highest gross pay (or None if empty)
        if not self.employees:
            return None
        return max(self.employees, key=lambda emp: emp.gross_pay)

    def find_lowest_paid(self):
        # TODO: return the Employee with the lowest gross pay (or None if empty)
        if not self.employees:
            return None
        return min(self.employees, key=lambda emp:emp.gross_pay)

    def get_employee_count(self):
        # TODO
        return len(self.employees) 

    def calculate_average_pay(self):
        # TODO: return total / count, or 0.0 if empty
        if self.count > 0:
            return self.total / self.count
        else:
            return 0.0
