
#---------------------------Single Inheritance--------------------------------

class Parent:
    def __init__(self, parent_name="Default Parent"):
        self._parent_name = parent_name 

    def get_parent_name(self):
        return self._parent_name

    def set_parent_name(self, name):
        self._parent_name = name

    def func1(self):
        print(f"Parent Class: Hello from {self._parent_name}.")


class Child(Parent):
    def __init__(self, parent_name="Default Parent", child_name="Default Child"):
        super().__init__(parent_name)
        self._child_name = child_name 

    def get_child_name(self):
        return self._child_name

    def set_child_name(self, name):
        self._child_name = name

    def func2(self):
        print(f"Child Class: Hello from {self._child_name}, child of {self.get_parent_name()}.")


# --- kaiza experimenting with objects ---


obj1 = Child("Arthur", "Bob")
obj1.func1()  
obj1.func2() 

print("-" * 40)


obj1.set_parent_name("Victoria")
obj1.set_child_name("Charlie")

print("After updating values:")
obj1.func1()
obj1.func2()

print("-" * 40)


obj2 = Child("Diana", "Ethan")
obj2.func1()
obj2.func2()


#---------------------------MULTIPLE INHERITANCE--------------------------------------

class Mother:
    def __init__(self):
        self.mothername = ""

    def get_mothername(self):
        return self.mothername

    def set_mothername(self, name):
        self.mothername = name


class Father:
    def __init__(self):
        self.fathername = ""

    def get_fathername(self):
        return self.fathername

    def set_fathername(self, name):
        self.fathername = name


class Son(Mother, Father):
    def __init__(self):
        Mother.__init__(self)
        Father.__init__(self)

    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


#===== kaiza experiments pt.2 ======
s1 = Son()
s1.set_fathername("RAM")
s1.set_mothername("SITA")
s1.parents()




#---------------------------MULTILEVEL INHERITANCE------------------------------

class Grandfather:
    def __init__(self, grandfathername=""):
        self.grandfathername = grandfathername


class Father(Grandfather):
    def __init__(self, fathername="", grandfathername=""):
        super().__init__(grandfathername)
        self.fathername = fathername


class Son(Father):
    def __init__(self, sonname="", fathername="", grandfathername=""):
        super().__init__(fathername, grandfathername)
        self.sonname = sonname

    def print_name(self):
        print("Grandfather name :", self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


# ====== kaiza experiments pt3 =======
s1 = Son("Prince", "Rampal", "Lal mani")
print(s1.grandfathername)
s1.print_name()    

#----------------------------HIERARCHAL INHERITANCE-------------------------------------------

class Parent:
    def __init__(self, name="Default Parent"):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def func1(self):
        print(f"This function is in parent class. Owner: {self._name}")


class Child1(Parent):
    def __init__(self, parent_name="Default Parent", child_name="Child 1"):
        super().__init__(parent_name)
        self._child_name = child_name

    def get_child_name(self):
        return self._child_name

    def set_child_name(self, name):
        self._child_name = name

    def func2(self):
        print(f"This function is in child 1. Name: {self._child_name}")


class Child2(Parent):
    def __init__(self, parent_name="Default Parent", child_name="Child 2"):
        super().__init__(parent_name)
        self._child_name = child_name

    def get_child_name(self):
        return self._child_name

    def set_child_name(self, name):
        self._child_name = name

    def func3(self):
        print(f"This function is in child 2. Name: {self._child_name}")


# ====== dr doofenshmkaiza incorporated =======
object1 = Child1("Root Family", "Alice")
object2 = Child2("Root Family", "Bob")

# testing Child1
object1.func1()[cite: 5]
object1.func2()[cite: 5]

print("-" * 40)

# testing Child2
object2.func1()[cite: 5]
object2.func3()[cite: 5]

# modifying values using setters
print("-" * 40)
object1.set_child_name("Alicia")
print("Updated Child 1 name:", object1.get_child_name())


#----------------------------- HYBRID INHERITANCE ---------------------------------

class School:
    def __init__(self, school_name="Default School"):
        self._school_name = school_name

    def get_school_name(self):
        return self._school_name

    def set_school_name(self, name):
        self._school_name = name

    def func1(self):
        print(f"This function is in school: {self._school_name}")


class Student1(School):
    def __init__(self, school_name="Default School", name1="Student One"):
        super().__init__(school_name)
        self._name1 = name1

    def get_name1(self):
        return self._name1

    def set_name1(self, name):
        self._name1 = name

    def func2(self):
        print(f"This function is in student 1: {self._name1}")


class Student2(School):
    def __init__(self, school_name="Default School", name2="Student Two"):
        super().__init__(school_name)
        self._name2 = name2

    def func3(self):
        print(f"This function is in student 2: {self._name2}")


class Student3(Student1, School):
    def __init__(self, school_name="Default School", name1="Student One", name3="Student Three"):
        Student1.__init__(self, school_name, name1)
        self._name3 = name3

    def get_name3(self):
        return self._name3

    def set_name3(self, name):
        self._name3 = name

    def func4(self):
        print(f"This function is in student 3: {self._name3}")


# ========= kaiza experiments pt.5
obj = Student3("Greenwood High", "Alice", "Bob")
obj.func1()[cite: 6] # Inherited from School
obj.func2()[cite: 6] # Inherited from Student1
obj.func4() # Defined in Student3

print("-" * 40)

# using setters to modify data
obj.set_school_name("Oakridge Academy")
obj.func1()

