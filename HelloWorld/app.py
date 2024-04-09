# Python is an enterpretor which means it runs the code line by line.
print('hello world')
print('o----')
print(' ||||')
print('*' * 10)

# strings are just a bunch of charactors in quotations
# an expression is code that produces a value * 10
# operators are the same as in math (*,+,-,/)

#variables temp stores data in memory
price = 10

#the variable "price" is defined as "10"
print (price) # dont put quotes when using variables because it will print the variable name instead of the stored data.
#changing the value further down the code line will make it change when printed.

#an interger is a number
#floating point number (float) is a decimal
rating = 4.9

#variables can contain strings
name = "Damori"

#boolean is True/False
is_published = False #python is case sensitive



#ACTIVITY
# We check in a patient named John Smith.
# He is 20 y/o and is a new patient.
# Define 3 variables
    #name
    #age
    #and if they are a new patient

name = 'Smith, John'
age = 20
is_new_patient = True


print (name, age, is_new_patient)




#HOW TO RECIEVE INPUT FROM USER
#print and input are a couple of many functions
#functions make code do stuff

name = input('What is your name? ')

#this whill ask user for input and store it in variable "name"
print("Hi " + name) #concatonating is when you shrink multiple lines of code into one line.


#ACTIVITY
#Make an expression that askes their name and favorite color.
#then print that in a sentence

name = input ('What is your name? ')
fav_color = input ('what is your favorite color? ')

print (name + ' likes ' + fav_color)