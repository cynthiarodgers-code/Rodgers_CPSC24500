"""
payroll_report.py - Week 4

PayrollReport handles all display and file output. It does not store data itself --
it gets data from the PayrollProcessor passed into its constructor.
"""

class PayrollReport:

    def __init__(self, processor):
        # TODO: store the processor
        self._processor = processor
    
    def display_all_employees(self):
        # TODO: print a header row, then each employee on its own line
        
        print("\n --- Employee Data ---")
        print(f"{'ID':<10} {'Name':<20}")
        print("-" * 30)

        for emp in self._processor.employees:
           print(f"{emp.employee_id:<10} {emp.name:<20}")
        
        

    def display_payroll_summary(self):
        # TODO: print total employees, total payroll, average pay,
        #       highest paid, lowest paid
        employees = self._processor.employees
        if not employees:
            print("No employees to summarize.")
            return
        
        salaries = [employee.hourly_rate for employee in employees]
    
        total_employees = len(employees)
        total_payroll = sum(salaries)
        average_pay = total_payroll / total_employees
        highest_paid = max(salaries)
        lowest_paid = min(salaries)

        print("-" * 30)
        print("      PAYROLL SUMMARY      ")
        print("-" * 30)
        print(f"Total Employees: {total_employees}")
        print(f"Total Payroll:   ${total_payroll:.2f}")
        print(f"Average Pay:     ${average_pay:.2f}")
        print(f"Highest Paid:    ${highest_paid:.2f}")
        print(f"Lowest Paid:     ${lowest_paid:.2f}")
        print("-" * 30)
        
    def generate_report_file(self, filename):
        # TODO: write the full report (employees + summary) to a text file
        # Use a `with` block

          with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*40 + "\n")
            f.write("EMPLOYEE REPORT\n")
            f.write("="*40 + "\n\n")
        
            f.write(f"{'ID':<10} | {'Name':<20}\n")
            f.write("-" * 40 + "\n")
            
            for emp in self._processor.employees:
                f.write(f"{emp.employee_id:<10} | {emp.name:<20}\n")
        
            print(f"Report successfully generated: {filename}")



