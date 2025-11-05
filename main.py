class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        first, last = value.split()
        self.first_name = first
        self.last_name = last

p1 = Person("Hasan", "Aliyev")
print(p1.full_name)  

p1.full_name = "Jasur Karimov"
print(p1.first_name) 
print(p1.last_name)  
print(p1.full_name)
