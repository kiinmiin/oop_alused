"""Student class with student name and grades."""


class Student:
    
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.id = None
        
    def set_id(self, id):
        if self.id is None:
            self.id = id
            
    def get_id(self):
        return self.id
        
    def get_grades(self):
        return self.grades
        
    def add_grade(self, course, grade: int):
        self.grades.append((course, grade))
        
    def get_average_grade(self):
        if len(self.grades) == 0:
            return -1
        else:    
            total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)
        
    def __repr__(self):
        return self.name
    pass
