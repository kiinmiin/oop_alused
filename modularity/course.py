"""Course class with name and grades."""


class Course:
    def __init__(self, name: str):
        self.name = name
        self.grades = []
    
    def add_grade(self, student, grade: int):
        self.grades.append((student, grade))
        
    def get_grades(self):
        return self.grades
        
    def get_average_grade(self) -> float:
        if len(self.grades) == 0:
            return -1
        else:
            total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)
        
    def __repr__(self):
        return self.name
    pass