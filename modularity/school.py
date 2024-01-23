"""School class which stores information about courses and students."""


class School:
    
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []
        
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            
    def add_student(self, student):
        if student not in self.students:
            student.set_id(len(self.students) + 1)
            self.students.append(student)
            
    def add_student_grade(self, student, course, grade):
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)
            
    def get_students(self):
        return self.students
        
    def get_courses(self):
        return self.courses
        
    def get_students_ordered_by_average_grade(self):
        return sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)
    pass
