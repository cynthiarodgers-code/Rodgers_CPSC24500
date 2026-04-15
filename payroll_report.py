"""
payroll_report.py - Week 4

PayrollReport handles all display and file output. It does not store data itself --
it gets data from the PayrollProcessor passed into its constructor.
"""


class PayrollReport:

    def __init__(self, processor):
        # TODO: store the processor
        self.processor = processor
        

    def display_all_employees(self):
        # TODO: print a header row, then each employee on its own line

        print(f'{'ID' :<5} {'Name' :<20}')
        # Use self._processor.employees to get the list

        for employee in self.processor.employees:
            print(employee)

        

    def display_payroll_summary(self):
        # TODO: print total employees, total payroll, average pay,
        #       highest paid, lowest paid

        if not self.employees:
            print("Payroll Summary: No employees found.")
            return
        
        salaries = [emp.salary for emp in self.employees]
    
        total_employees = len(salaries)
        total_payroll = sum(salaries)
        average_pay = total_payroll / total_employees
        highest_paid = max(salaries)
        lowest_paid = min(salaries)

        print("-" * 30)
        print("      PAYROLL SUMMARY      ")
        print("-" * 30)
        print(f"Total Employees: {total_employees}")
        print(f"Total Payroll:   ${total_payroll:,.2f}")
        print(f"Average Pay:     ${average_pay:,.2f}")
        print(f"Highest Paid:    ${highest_paid:,.2f}")
        print(f"Lowest Paid:     ${lowest_paid:,.2f}")
        print("-" * 30)
        
    def generate_report_file(self, filename):
        # TODO: write the full report (employees + summary) to a text file
        # Use a `with` block

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*40 + "\n")
            f.write("EMPLOYEE REPORT\n")
            f.write("="*40 + "\n\n")
        
            f.write(f"{'ID':<10} | {'Name':<20} | {'Salary':<10}\n")
            f.write("-" * 40 + "\n")
            for emp in self.employees:
                f.write(f"{emp.id:<10} | {emp.name:<20} | ${emp.salary:,.2f}\n")
            
            f.write("\n" + "="*40 + "\n")
            f.write("SUMMARY\n")
            f.write("="*40 + "\n")

            summary = self.calculate_summary() 
            f.write(f"Total Employees: {summary['total_count']}\n")
            f.write(f"Total Payroll:   ${summary['total_payroll']:,.2f}\n")
            f.write(f"Average Salary:  ${summary['average_salary']:,.2f}\n")
        
        print(f"Report successfully generated: {filename}")



