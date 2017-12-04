import csv

from component.Employee import Employee
from component.Relationship import Relationship

class CsvReader:

    def readEmployee(self):
        nodeList = []
        csv_file =  open('/home/toprak/projects/python/sna-employee-manager-analysis/resources/nodes.csv', 'r')
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            nodeList.append(Employee(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))
        return nodeList


    def readRelationship(self, relationType):
        relationshipList = []
        csv_file = open('/home/toprak/projects/python/sna-employee-manager-analysis/resources/' + relationType + '.csv',
                        'r')
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            relationshipList.append(Relationship(line[0], line[1], line[2], relationType))
        return relationshipList

