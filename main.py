#    polymorphism with inheritance

class Patients:

    def type(self):
        print("These are our patients")
    
    def age(self):
        print("These are the patient's ages")

    def location(self):
        print("Our patients live in this locations")

class Healthy(Patients):
    def age(self):
        print("Healthy patient's ages")

class Sick(Patients):
     def age(self):
        print("Sick patient's ages")

#    create our objects

obj1 = Patients()
Melvin = Healthy()
Kate = Sick()

#   accessing the methods
obj1.type()
obj1.age()
obj1.location()

Melvin.type()
Melvin.age()
Melvin.location()

Kate.type()
Kate.age()
Kate.location()




    