# Collect Nabiha's Salary Details

def collect_salary_details():
    print("Hello Nabiha, Welcome to your salary allocation program.")
    
    salary = float(input("Enter your salary for the month: "))
    month = input("Enter the month: ")
    
    savings_percentage = float(input("Enter percentage for savings: "))
    rent_percentage = float(input("Enter percentage for rent: "))
    electricity_percentage = float(input("Enter percentage for electricity: "))
    
    extra_savings = float(input("Enter the additional savings amount: "))
    
    return salary, month, savings_percentage, rent_percentage, electricity_percentage, extra_savings

def calculate_allocations(salary, savings_percentage, rent_percentage, electricity_percentage, extra_savings):
    savings = (savings_percentage / 100) * salary
    rent = (rent_percentage / 100) * salary
    electricity = (electricity_percentage / 100) * salary
    
    expenses = savings + rent + electricity
    remaining_salary = salary - expenses
    yearly_rent_electricity = (rent + electricity) * 12
    salary_squared = salary ** 2 #Just for fun 
    
    saving_divided = savings / extra_savings if extra_savings  != 0 else 0 #avoid division by 0
    
    return savings, rent, electricity, expenses, remaining_salary, yearly_rent_electricity, salary_squared, extra_savings, saving_divided

def display_results(month, salary, savings, rent, electricity, expenses, remaining_salary, yearly_rent_electricity, salary_squared, extra_savings, savings_divided):
    # Display the result 
    print("-------------------------------------")
    print(f"Salary Allocation Report For {month}")
    print("-------------------------------------")
    print("Tatal Salary:", salary)
    print("Savings:", savings)
    print("Rent:", rent)
    print("Electricity:", electricity)
    print("Total Expenses:", expenses)
    print("Remaining Salary:", remaining_salary)
    print("Estimated Yearly Rent & Electricity:", yearly_rent_electricity)
    print("Salary Squared:", salary_squared)
    print("Extra Savings:", extra_savings)
    print("Savings Divided by Extra Savings:", savings_divided)
    print("--------------------------------------")
    
if __name__ == "__main__":
    salary, month, savings_percentage, rent_percentage, electricity_percentage, extra_savings = collect_salary_details()
    calculations = calculate_allocations(salary, savings_percentage, rent_percentage, electricity_percentage, extra_savings)
    display_results(month, salary, *calculations)