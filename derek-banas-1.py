import random
import sys
import os

# print("\n\nThis is how you print a string:")
print("\nHello World!")

# name = "Derek\n"
# print(name);

# single line comment
'''
this is how you make a multi-line comment

common data types:
numbers
strings
list
tuples

operators:
addition +
subtraction -
multiplication *
division /
modulus %
exponential **
remainder //
'''
#
# print("5 + 2 = ", 5+2)
# print("5 - 2 = ", 5-2)
# print("5 * 2 = ", 5*2)
# print("5 / 2 = ", 5/2)
# print("5 % 2 = ", 5%2)
# print("5 ** 2 = ", 5**2)
# print("5 // 2 = ", 5//2, "\n\n")

'''
    order of operation
    ()
    BODMAS
'''

# more on strings

# quote = "\"Always remember you are unique"
#
# multi_line_quote = ''' just
# like everyone else'''
#
# print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
#
# print('\n' * 5)
#
# print("I don't like ", end="")
# print("newlines")

# grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
# print('first Item', grocery_list[0])
#
# print(grocery_list[1:3])
#
# other_events = ['Wash Car', 'Pick up kids', 'Cash Check']
#
# to_do_list = [other_events, grocery_list]
# print(to_do_list)
# print(to_do_list[1][1])
#
# grocery_list.append('Onions')
# print(to_do_list)
# print(to_do_list[1][to_do_list[1].__len__()-1])
#
# grocery_list.insert(1, "Pickle")
# print(grocery_list)
# grocery_list.remove("Pickle")
# grocery_list.sort()
#
# del grocery_list[4]
# print(to_do_list)

# pi_tuple = (3, 1, 4, 1, 5, 9)
#
# new_tuple = list(pi_tuple)
# new_list = tuple(new_tuple)
#
# print(len(new_list))
# print(min(new_list))
# print(max(new_list))

# blacklist = {'Fiddler': 'Isaac Bowin',
#              'Captain Cold': 'Leonard Snart',
#              'Weather Wizard': 'Mark Mardon',
#              'Mirror Master': 'Sam Scudder',
#              'Pied Piper': 'Thomas Peterson'}
#
# print(blacklist['Pied Piper'])
#
# del blacklist['Mirror Master']
#
# print(blacklist)
#
# blacklist['Pied Piper'] = 'Hartley Rathaway'
#
# # print(blacklist['Pied Piper'])
#
# print(len(blacklist))
#
# print(blacklist.get("Pied Piper"))
#
# print(blacklist.keys())
# print(blacklist.values())

# age = 21
# insane = True
#
# if age > 16:
#     print('you are old enough to drive')
# else:
#     print('you are not old enough to drive')
#
# if age >= 21 or False:
#     print('you are old enough to drive a tractor trailer')
# elif age >= 16 and insane:
#     print('you are old enough to drive a car')
# else:
#     print('you are not old enough to drive at all')

# for x in range(0, 10):
#     print(x, ' ', end="")
#
# print()
#
# grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
#
# for anItem in grocery_list:
#     print(anItem)
#
# for z in range(2,11,2):
#     print(z, ' ', end="")
#
# print('\n')
#
# num_list=[[1,2,3], [10,20,30], [100,200,300]]
# for row in range(0, len(num_list)):
#     for column in range(0, len(num_list[0])):
#         print(num_list[row][column], ' ', end="")
#     print('')
#
#
# random_num = random.randrange(0, 100)
#
# while random_num != 15:
#     print(random_num, ' ', end="")
#     random_num = random.randrange(0, 100)

# i = 0
# while i <= 20:
#     if (i % 2) == 0:
#         print(i, " is even.")
#     elif i == 9:
#         break
#     else:
#         i += 1
#         continue
#
#     i += 1
#


# def add_number(f_num, l_num):
#     sum_num = f_num + l_num
#     return sum_num
#
#
# # print(add_number(1, 4))
# string = add_number(1, 4)
# print(string)

# print('What is your name?')
#
# your_name = sys.stdin.readline()
#
# print('Hello', your_name)

# long_string = "I'll catch you if you fall - The Floor"

# print(long_string[0-4])
# print(long_string[-5:])
# print(long_string[:-5])
# print(long_string[:4] + " be there")
# print("%c is my %s letter and my number %d is %.5f" % ('x', 'favorite', 1, .14))

# print(long_string.capitalize())
# print(long_string.find('Floor'))
# print(long_string.isalpha())
# print(long_string.isalnum())
# print(len(long_string))
# print(long_string.replace("Floor", "Ground"))
# print(long_string.strip())
# quote_list = long_string.split(" ")
# print(quote_list)

# test_file = open("test.txt", "ab+")
#
# print(test_file.mode)
# print(test_file.name)
# test_file.write(bytes("Write me to the file\n", "UTF-8"))
# test_file.close()
#
# test_file = open("test.txt", "r+")
# text_in_file = test_file.read()
# print(text_in_file)
# test_file.close()
#
# os.remove("test.txt")

class Animal:
    _name = None
    __height = 0
    _weight = 0
    _sound = 0

    def __init__(self, name, height, weight, sound):
        self._name = name
        self.__height = height
        self._weight = weight
        self._sound = sound

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self._weight = weight

    def get_weight(self):
        return self._weight

    def set_sound(self, sound):
        self._sound = sound

    def get_sound(self):
        return self._sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self._name, self.get_height(), self._weight, self._sound)


cat = Animal('Whiskeys', 33, 10, 'meow')
print(cat.toString())


class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {} and his owner is {}".format(self._name, self.get_height(), self._weight, self._sound, self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print((self.get_sound() + " \n") * how_many)

    def __repr__(self):
        return "{} is {} cm tall and {} kilograms and says {} and his owner is {}".format(self._name, self.get_height(), self._weight, self._sound, self.__owner)


spotty = Dog("Spotty", 53, 27, "Ruff", "Justin")
print(spotty.toString())

hasuky = Dog("Hasuky", 60, 45, "Awoo", "Gerard")
print(hasuky)

class AnimalTestType:
    def get_type(self, animal):
        animal.get_type()

test_animal = AnimalTestType()
test_animal.get_type(cat)
test_animal.get_type(spotty)
test_animal.get_type(hasuky)

hasuky.multiple_sounds(10)
hasuky.multiple_sounds()
