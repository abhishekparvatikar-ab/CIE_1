
import sys

salary = int(sys.argv[1])

if salary < 20000:
    Bonus = salary * 0.05
elif salary < 40000:
    Bonus = salary * 0.10
else:
    Bonus = salary * 0.15

total_salary = salary + Bonus

print("Enter the Salary:", salary)
print("The Bonus :", Bonus)
print("The Total Salary is:", total_salary)
