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

    processor = PayrollProcessor()
    
    with open("employees.txt", "w") as f:
        f.write("101,Alice,20.0,45\n102,Bob,25.0,40\n103,Charlie,15.0,30\n")
        
        processor.load_from_file("employees.txt")

        report = PayrollReport(PayrollProcessor)

        while True:
            print("\n--- Payroll Menu ---")
            print("1. View all employees")
            print("2. View payroll summary")
            print("3. Generate report file")
            print("4. Quit")
        
            choice = input("Enter choice (1-4): ")

            if choice == '1':
                report.display_all_employees()
            elif choice == '2':
                report.display_payroll_summary()
            elif choice == '3':
                report.generate_report_file()
            elif choice == '4':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
