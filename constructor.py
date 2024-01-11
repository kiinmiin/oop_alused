"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""
    
    pass


class Person:
    """Represent person with firstname, lastname and age."""
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0
    pass


class Student:
    """Represent student with firstname, lastname and age."""
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    pass


if __name__ == '__main__':
    # empty object/usage
    empty = Empty()
    # 3 x person object/usage
    person1 = Person()
    person1.firstname = 'Kadi'
    person1.lastname = 'Lepp'
    person1.age = 16
    person2 = Person()
    person2.firstname = 'Aru'
    person2.lastname = 'Mati'
    person2.age = 17
    person3 = Person()
    person3.firstname = 'Anti'
    person3.lastname = 'Arjukese'
    person3.age = 18
    # 3 x student object/usage
    student1 = Student("Mati", "Maasikas", 15)
    student2 = Student("Ülo", "Alo", 16)
    student3 = Student("John", "Doe", 18)
    
    pass
