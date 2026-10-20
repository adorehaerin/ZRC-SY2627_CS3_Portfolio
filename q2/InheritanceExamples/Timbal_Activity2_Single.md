
#Single Inheritance

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
