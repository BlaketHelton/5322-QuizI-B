'''
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iterate through the dictionary to print out their name and thier new salary (as shown in the image)
'''


import csv

#open the file
csv_file = open ('employee_data.csv', 'r')
csv_reader = csv.reader(csv_file)
next(csv_reader)



#create an empty dictionary
new_employee_data = {}

#use a loop to iterate through the csv file
for row in csv_reader:
        # Check if security clearance is TS
    if row[9] == 'TS':
        first_name = row[1]
        last_name = row[2]
        # Get the old salary
        old_salary = float(row[5])
        # Calculate the new salary
        new_salary = old_salary * 1.1
        # Add the employee name and new salary to the dictionary
        new_employee_data[row[0]] = new_salary
        print(f'Employee Name: {first_name} {last_name} Current Salary: ${old_salary:.2f}')


    #check if the employee fits the search criteria


#print(f'Employee Name: {first_name} {last_name} Current Salary: ${old_salary:.2f}')


print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per image
total_difference = 0

for employee, new_salary in new_employee_data.items():
    # Get the employee name from the dictionary
    first_name = employee[1]
    last_name = employee[2]
    # Print out the employee name and their new salary
    print(f'Employee Name: {first_name} {last_name} New Salary: ${new_salary:.2f}')
    # Calculate the difference between the old salary and new salary
    difference = new_salary - old_salary
    total_difference += difference

print()
print('=========================================')
print()

#print out the total difference between the old salary and the new salary as per image.

# Calculate the difference between the old and new salary
difference = new_salary - old_salary
 # Add the difference to the total difference
total_difference += difference

# Print out the total difference
print(f'Total increase in salary: ${total_difference:.2f}')
        
csv_file.close()

