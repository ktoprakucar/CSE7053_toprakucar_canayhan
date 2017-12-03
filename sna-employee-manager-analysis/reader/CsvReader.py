import csv

from component.Employee import Employee

with open('/home/toprak/projects/python/sna-employee-manager-analysis/resources/nodes.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    employeeList = []

    for line in csv_reader:
        employeeList.extend(Employee(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))


print("blablabla")