"""Simple class."""
class Student:
    
    def __init__(self, name):
        """Student class construct.
        
        Creates student type object.
        
        Parameters:
        Name (str): Name of student.
        """
        self.name = name
        self.finished = False
        