Salary=("Enter the Salary: ");
salary = int(sys.argv[1])
if salary < 20000:
    S=salary * 0.05
elif salary < 40000:
    S=salary * 0.1
else: 
    S=salary * 0.15

print("The Salary is: ", salary)
print("The Bonus %: ", Bonus)
print("Enter the total Salary: ", salary) 