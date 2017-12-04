class Employee:
    def __init__(self, id, departmentName, departmentId, isManager, managerId, superDepartmentId, isActive):
        self.id = id
        self.departmentName = departmentName
        self.departmentId = departmentId
        self.isManager = isManager
        self.managerId = managerId
        self.superDepartmentId = superDepartmentId
        self.isActive = isActive
