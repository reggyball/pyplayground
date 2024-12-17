#### GENERAL FORMAT OF CLASS ####

# class NameofClass:
#     content1_of_class
#     content2_of_class

# class MyFirstClass:
#     pass

# #two distint instances of class MyFirstClass
# a = MyFirstClass()
# b = MyFirstClass()

# #to prove the instances are unique, print the memory address of the instances
# print(a)
# print(b)

# # -----------------------------------------examples
# class cat:
#     'cat class'
#     def __init__(self, name, age):   
#         'initialze cat name and age'                                 #initializer of attributes
#         self.name = name                                             # Assign the name attribute to the instance
#         self.age = age                                               # Assign the age attribute to the instance

#     def greet(self):
#         'Greets cat'
#         print(f"Hi, {self.name}, you look young to be {self.age} years old!")

#     def birthday(self):
#         'Adds 1 to age and greets cat'
#         self.age += 1
#         print(f"Happy Birthday {self.name}, you are now {self.age} years old!") 
    
#     def treats(self, treat):
#         print(f"As a treat, mom will give you {treat}, my dear {self.name}!")


# #instances of class cat
# cat1 = cat('Appa', 3)
# cat2 = cat('x', 1)

# print(cat1)             #prints object address

# print(cat1.name)        #prints name attribute of instance 'cat1'
# print(cat1.age)         #prints age attribute of instance 'cat1'

# #accesing instances -------------------
# print(cat2.name)        #prints X      
# cat2.name = "Sunny"      #reassign attribute name of instance cat2 to "Sunny"
# print(cat2.name)        #prints reassigned name

# ## access methods ---------------
# cat1.greet()            #syntax <instance>.<method>()
# cat2.birthday()
# cat1.treats('sushi')

# #docstrings
# # help(cat)

#ENCAPSULATION
# ####################### VET HOSPITAL #########################################
# import datetime

# class Pet:
#     '''
#     Pet is an object that exhibits the characteristics and behaviors of a pet.
#     '''

#     def __init__(self, name, year_born, species):
#         self.__name = name
#         self.__year_born = year_born
#         self.__species = species
    
#     def __compute_age(self):
#         today = datetime.datetime.now()
#         return today.year - self.__year_born

#     def get_pet_details(self):
#         pet_details = {"Name": self.__name, "species": self.__species, "age": self.__compute_age()}
#         return pet_details

# class VetHospital:
#     '''
#     VetHospital is an object that exhibits the characteristics and behaviors of the clinic.
#     '''

#     def __init__(self, name):
#         self.__name = name
#         self.__patients = []
    
#     def get_name(self):
#         return self.__name

#     def admit_pet(self, pet):
#         self.__patients.append(pet)

#     def discharge_pet(self, pet):
#         self.__patients.remove(pet)

#     def get_patient_info(self, pet):
#         if pet in self.__patients:
#             return pet.get_pet_details()
#         return {}

#     def get_all_patient_info(self):

#         all_patient_info = []
#         for pet in self.__patients:
#             all_patient_info.append(self.get_patient_info(pet))
#         return all_patient_info


# vet_hospital = VetHospital ("Wonderful Pets Veterinary Hospital")
# pet1 = Pet ("Ranger", 2023, "Bird")
# pet2 = Pet ("Oreo", 2015, "Dog")
# pet3 = Pet ("Jpeg", 2014, "Dog")
# pet4 = Pet ("Blankie", 2022, "Cat")

# #admitpets
# vet_hospital.admit_pet(pet1)
# vet_hospital.admit_pet(pet2)
# print("Current patients:", vet_hospital.get_all_patient_info())

# #get info of a patient
# print(vet_hospital.get_patient_info(pet1))

# #discharge a pet
# vet_hospital.discharge_pet(pet2)
# print("Current patients: ", vet_hospital.get_all_patient_info())

#################################################################
# #INHERITANCE

# #superclass
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
    
#     def eat (self):
#         print(f"{self.name} is eating.")

#     def sleep (self):
#         print(f"{self.name} is sleeping")


# #subclass
# class Mammal(Animal):
#     def __init__(self, name, species, fur_color):
#         super().__init__(name, species)
#         self.fur_color = fur_color

#     def give_birth(self):
#         print(f"{self.name} is giving birth.")

# class Bird(Animal):
#     def __init__(self, name, species, wingspan):
#         super().__init__(name, species)
#         self.wingspan = wingspan
    
#     def fly(self):
#         print(f"{self.name} is flying with a wingspan of {self.wingspan}")


# #create instances
# Appa = Mammal("Appa", "Cat", "White")
# Theo = Bird("Theo", "Cat", "30cm")

# #access methods in superclass
# Appa.sleep()
# Theo.eat()

# #access using dot notation, attributes and methods in subclass
# print(f"{Appa.name}'s fur color is {Appa.fur_color}")
# print(f"{Theo.name}'s wingspan is {Theo.wingspan}")
# Appa.give_birth()
# Theo.fly()

###############################################
#INHERITANCE WITH ACCESS MODIFIERS
#superclass
class Animal:
    def __init__(self, name, species):
        self.__name = name                         #private attribute
        self._species = species                    #protected attribute
    
    def eat (self):
        print(f"{self.__name} is eating.")

    def sleep (self):
        print(f"{self.__name} is sleeping")

    def get_name(self):                             #accessor fucntion
        return self.__name


#subclass
class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"{self.get_name()}, {self._species} is giving birth.")

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan
    
    def fly(self):
        print(f"{self.get_name()}, {self._species} is flying with a wingspan of {self.wingspan}")

#Create Instances
Appa = Mammal("Appa", "Cat", "White")
Theo = Bird("Theo", "Cat", "30cm")

Appa.give_birth()
Theo.fly()