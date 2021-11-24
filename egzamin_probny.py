"""Zadanie 1"""
from math import pi

def calc_circle_area(r):
    print(r * r * pi)

calc_circle_area(5)

"""Zadanie 2"""

def check_parity():
    number1 = int(input("Podaj liczb :"))
    if number1 % 2 == 0 :
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieprazysta")


check_parity()

"""Zadanie 3"""

def element_present (number2, array):
    if number2 in array:
        print(True)
    else:
        print(False)


element_present(8, [1,2,5,6,9,11])

"""Zadanie 4 """

def check_str_len():
    string1 = input("Podaj string: ")
    try:
        if len(string1) < 8:
            raise ValueError
        else:
            print("OK")

    except ValueError:
        print("ValueError")


check_str_len()

"""Zadanie 5"""

slownik = {}


def print_menu():
    print("1. Dodaj wpis: ")
    print("2. Odzyskaj wpis: ")
    print("3. Zmodyfikuj wpis: ")
    print("4. Usun wpis: ")
    print("0. Wyjdz: ")

def create_item(dict1, key, value):
    #print(slownik)
    dict1[key]= value
    #print(slownik)

def read_item():
    print(slownik)

def update_item(dict1, key, update_value):
    #print(dict1)
    dict2 = {key: update_value}
    dict1.update(dict2)
    #print(dict1)

def delete_item(dict1, key):
     #print(dict1)
    dict1.pop(key)
    #print(dict1)

    
while True:
    print_menu()
    option = input('Podaj opcja :')
    if option == "1":
        create_item(slownik, input("Podaj key:"), input('Podaj value '))

    elif option == '2':
        read_item()

    elif option == '3':
        update_item(slownik, input('Podaj key'), input('Podaj nowe value'))

    elif option == "4":
        delete_item(slownik, input("Podaj key "))

    elif option == "0":
        break

"""Zadanie 6 """

class Animal:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        print(self.name)

    def set_name(self,name):
        self.name = name 

class Mammal(Animal):
    def __init__(self, no_legs, has_fur):
        super.__init__(name)
        self.no_legs = no_legs
        self.has_fur = has_fur

    def get_no_legs(self):
        print(self.no_legs)

    def set_no_legs(self, no_legs):
        self.no_legs = no_legs

    def get_has_fur(self):
        print(self.has_fur)

    def set_has_fur(self, has_fur):
        self.has_fur = has_fur

class Canine(Mammal):
    def __init__(self, no_legs, has_fur, howl, bark):
        super().__init__(no_legs, has_fur, howl, bark)
        self.howl = howl
        self.bark = bark

class Dog(Canine):
    def __init__(self, no_legs, has_fur, howl, bark, kind, owner):
        super().__init__(no_legs, has_fur, howl, bark, kind, owner)

    def get_kind(self):
        print(self.get_kind)

    def set_kind(self, kind):
        self.kind = kind

    def get_owner(self):
        print(self.get_owner)

    def set_owner(self, owner):
        self.owner = owner
        


