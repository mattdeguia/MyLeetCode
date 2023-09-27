# imports:
import math;


# ---------------------------------------------------------------

"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    SUMMARY:
    - 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

# QUESTION: 

# main function:
if __name__ == "__main__":
    print("");

# ---------------------------------------------------------------



# output:
print("---------------------------------------------------");
print("OUTPUTS:");
print("Hello");                     # print with new line
print("Another sentence", end="");  # print without new line
print("");                          # print a new line
print("");                          # print a new line



# input from user:
print("---------------------------------------------------");
print("INPUTS:");
val = input("Enter a value: ");     # this way of getting input returns a string value
print(val);
print("");



# variables:
print("---------------------------------------------------");
print("VARIABLES:");
myString = "cheese";
myNum = 100;
print(myString, "and", myNum);
print("");



# operators:
print("---------------------------------------------------");
print("OPERATORS:");
y = 10;
y += 1;             # y = y + 1
y -= 1;             # y = y - 1
y *= 1;             # y = y * 1
y /= 1;             # y = y / 1
y %= 1;             # y = y % 1
y **= 2;            # y = y ^ 2
print(y);
print("");



# functions:
print("---------------------------------------------------");
print("FUNCTIONS:");
def my_function():                  # function declaration
    print("This is my function");
    print("");                      
my_function();                      # function call
print("");



# useful functions:
print("---------------------------------------------------");
print("OTHER FUNCTIONS:");
print(type(myNum));                 # check what type of data it is
x = str(myNum);                     # convert "myNum" from string to integer
print(type(x));
print("");                          # print a new line



# for loops:
print("---------------------------------------------------");
print("FOR LOOPS:");
fruits = ["apple", "banana", "carrot"];
for each_fruit in fruits:
    print(each_fruit);
print("");                          # print a new line



# while loops:
print("---------------------------------------------------");
print("WHILE LOOPS:");
i = 1;
while (i <= 5):
    print(i, " ", end="");
    i += 1;
print("");                          # print a new line
print("");



# if, if-else, and else statements
print("---------------------------------------------------");
print("IF STATEMENTS:");
a = 5;
b = 10;
if (a > b):
    print("a is greater than b");
elif (b > a):
    print("b is greater than a");
else:
    print("they are the same values");
print("");                          # print a new line



# classes and objects
print("---------------------------------------------------");
print("CLASSES AND OBJECTS:");
class Person:                       # create a class called Person
    def __init__(self, name, age):  # constructor for class
        self.name = name;
        self.age = age;

test = Person("John", 36);          # instantiate an object of class "Person"
print(test);                        # print memory address of object
print(test.name);                   # print specific properties of object
print(test.age);
print("");



# data structures: arrays, linked lists, trees
print("---------------------------------------------------");
print("DATA STRUCTURES:");
print("");


#________________________
print("Arrays:");
colors = ["blue", "red", "yellow", "purple"];       # array

print("All colors: ", end="")
for color in colors:                                # display all in array
    print(color, "", end="");
print("");
print("Amount of values in array: ", len(colors));  # get length of array

print("colors[0] = ", colors[0]);                   # display one value in array
colors[0] = "orange";                               # change a value in the array
print("colors[0] = ", colors[0]);

print("")

#________________________
print("Lists:");
things = ["apples", 1, "cheese", 2.0, True];
print(things);
print("");

#________________________
print("Tuples:");
moreThings = ("one", "two", "three");
print(moreThings);
print("");

#________________________
print("Dictionaries:");
myCar = {                                           # create a dictionary
  "brand": "Ford",                                  # key -> value
  "model": "Mustang",
  "year": 1964
}
print(myCar);                                       # print everything from dictionary
print("myCar['brand'] = ", myCar["brand"]);                              # print one value from the dictionary



print("");
print("");
print("");
print("");
print("");