# initialize the value of net income, gross income, total deduction, name of employee, pag-ibig contribution
net_income = 0
gross_income = 0
total_deduction = 0
employee_name = ""
department = ""
pagibig_contribution = 100.00
SSS_contribution = 0
philhealth_contribution = 0


# input the value of rate per hour, num hours per day, num of days per week, num of week per month
employee_name = str(input("Enter employee name:" ))
department = str(input("Enter department name:"))
rate_per_hour = float(input("Enter employee's rate per hour:"))
num_hours_per_day = float(input("Enter employee's hours per day:"))
num_days_per_week = int(input("Enter employee's days per week:"))
num_weeks_per_month = int(input("Enter employee's weeks per month:"))

# Setting the formula for gross income, total deduction, net income
gross_income = rate_per_hour * num_hours_per_day * num_days_per_week * num_weeks_per_month

# defining the pagibig contribution, sss and philhealth contribution based from the result of gross income

if 0 <= gross_income <= 20000:
    SSS_contribution = 125.75
    philhealth_contribution = 100
elif 20001 <= gross_income <= 50000:
    SSS_contribution = 2200.50
    philhealth_contribution = 1200
elif 50001 <= gross_income <= 75000:
    SSS_contribution = 4800
    philhealth_contribution = 6800
else:
    SSS_contribution = 5800
    philhealth_contribution = 8800

#computing the employee's net income
total_deduction = SSS_contribution + pagibig_contribution + philhealth_contribution
net_income = gross_income - total_deduction

# Display the computed value for employee name, department, net income, gross income, total deduction
print("Employee name:",employee_name)
print("Department:", department)
print("Net Income:",net_income)
print("Gross Income:",gross_income)
print("Total Deduction:",total_deduction)