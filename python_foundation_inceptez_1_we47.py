#Refer python_theory pdf/notes for understanding few basics of python...
'''
What we are going to learn in Python???
**1. Basic programming fundamentals -
A. Intent Block based coding
B. Comments
C. Quotes
D. Variables & Values
E. Naming Conventions

F. Types and Casting
G. Input & Output operations
H. Datatypes (Simple/premetive or Complex/Collection (data structure))

I. Operators
J. Conditional Structure
K. Looping Constructs
L. Complex Types

#Specific to Python
2. Exception Handling

3. **FBP - Dataengineers (eg. leverage the spark functions writtern by somebody)

4. OOPS - Framework developers (eg. commiters/contributors of apache spark)
5. Building Apps/APIs/AI integration using Python Programming

'''

'''
Interpreter
line/line -> compiler -> object code -> vm -> execute
Compiler
entire line -> compiler -> object code -> vm -> execute

#execution example of both
Interpreter Example:
vi python_interpreter.py
name='Inceptez'
age=11
print(name)
#print(something)
print(age)
print("hello")
print("good morning")

#Interpret the line by line of code and execute
python python_interpreter.py

vi scala_compiler.scala
object obj1 extends App
{
var name="Inceptez"
var age=11
println(name)
printlnxyz(age)
println("hello")
println("good morning")
println("thank u")
}

#Compile the complete code and execute
scalac scala_compiler.scala
scala obj1

'''

print("************** 1. Basics of Python Programing*************")
print("How to run a python program")
#right click this module tab and run the program or go to run menu and run or click on the play button in the right top
#keyboard shortcut - ctrl+shift+f10

#Fundamentals of Python Programming:
####################################
print("A. Python is an indent based programming language")
#Why Python uses indend based programing ->
#1. Managing the program more efficiently
#2. Better Readablility of the code
#3. For creating the hierarchy of programming.
#4. By default 4 spaces we will give for indends, but more/less spaces or tabs also can be used...

#Indendation is needed for (hierarchy of programming), because we are doing block operation (lines of code) with in the for loop using only intent not by using do or done or { }
aspirants_list=['Jeeva','Bharathi','Vaanmathy','Nag']
for aspirants in aspirants_list:
    print("good afternoon ",aspirants)
print("good after all aspirants")

#Linux is not an intend based program, it is a block based rather:
'''
for i in `ls`
do
        echo "hello"
echo $i
done
'''

#indendation has to be uniform within the block of code (not across the block of code)
#below prog doesnt work because we are using different number of spaces between lines of code in a given block
aspirants_list=['Jeeva','Bharathi','Vaanmathy','Nag']
for aspirants in aspirants_list:
    print("good afternoon ",aspirants)
     #print("Lets learn python")

#below program works if we have different intent maintained at different blocks
aspirants_list=['Jeeva','Bharathi','Vaanmathy','Nag']
for aspirants in aspirants_list:
    print("good afternoon ",aspirants)
    print("Lets learn python")
for aspirants in aspirants_list:
  print("Captial name of  ",aspirants.capitalize())

#optimal number of spaces has to be 4, but any numbers you can give
for aspirants in aspirants_list:
  print("Captial name of  ",aspirants.capitalize())

print("B. This is a commented line in Python")
#comments improve the understanding and usability of the code efficiently
#Comments are used for 2 purposes:
#1. For creating dead codes to avoid execution of the optional code
#2. For creating descriptions/information/commenting something about a line or block of code
#Comments are of 2 types:
#1. Single line comment - use # in the starting
'''2.Multi line comment''' # - use ''' comment ''' or """ comment """

print("C. Playing with Quotes: Python treats single quotes the same as double quotes as like triple quotes, but has some differences")
#Python treats single quotes the same as double quotes and triple quotes.
company1='inceptez'
company2="inceptez"
company3="""inceptez"""
print(company1,company2,company3)#python treat all as same

#Then why 3 notations?
#Double quotes is used for holding single quoted chars
#company1='inceptez's'#this will not work
company1="this is inceptez's property"
#vice versa - single inside double quotes
company2='This is "inceptez" company'

#Triple quotes (either '''/""") place very important roles
#For holding both single, double quoted data we can use triple quotes
company3="""This is "inceptez's" company's property"""
print(company1,company2,company3)#Hover the print function to understand how we can use comments with """

#For handling paragraph/multilines text, we can use 3 single or doublequotes
sql_query="""select * from tablename
where city='chennai'
order by id"""

#3 single or double quotes used for creating documentation/comments in functions eg. print("") hover or ctrl+click to understand

#Any programming language learning has to be started first learning about variables
print("Let's learn all about VARIABLES")
'''1. Variable Properties - Dynamic Inference, Dynamic Typed, Strongly Typed'''

#Dynamic inference - based on the assigned value to a variable, it will automatically decides/infer/identify/refers the data type dynamically
height=5.11
print(type(height))#float
weight=99
print(type(weight))#int

#Dynamically typed (Duck type): If a variable is created with a specific data type, can be changed later
weight=99
print(type(weight))#int
weight=weight+.350#float
print(type(weight))#float (dynamically changing the type from int to float)

'''Scala is a statically typed language
#below is not possible - because of statically type feature
var weight=99
weight=weight+.350#fails
weight=weight+1#works
'''

#Strongly typed: Python allow us to operate between the variables of same datatype (of the same hierarchy) and doesn't allow to operate between different datatypes.
name='irfan'
weight=99
#print(name+weight)#this will not work, because strongly typed

#In scala, weakly typed, it works...
'''
var name="irfan"
var weight=99
println(name+weight)#this works in scala, because weakly typed
'''

print("E. Naming Conventions")
#A variable can have camel case or init upper or with underscores


#A variable name must start with a letter or the underscore character

#A variable name cannot start with a number


#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )


#Variable names are case-sensitive


#Multiple Variables can be assigned in a single line (Multi Assignment)


print("F. Types & Casting")

#3. How to check a given TYPE is of what datatype we expect  & type casting
#Functions we are learning in this topic ()


#What we are learning here is the usage of few functions like
#To understand the age is of what type

#To check wheter the age is of an expected type

#To convert the age to an expected type


#Check for a given type, if it is not as expected then cast it to the expected type programatically using if condition


print("G. Standard Input & output options")
#assigning value statically

#assigning value dynamically using input()

#print statement will be used as a std output function
#semi colon can be used to seperate a statment if we write multiple statements in one line

#below print function is taking only 1 argument (but print can take any number of arguments)

#below print function is taking multiple arguments and printing them individually

#Formatted string Print statements - positional args
#Positional arguments

#keyword/named arguments

#Formatted string Print statements other way (3x onwards) - named args

print("H. Datatypes, Mutability & Builtin Functions")
#Sequence Types
#string type -
# indexed sequenced collection of characters/literals
# can be assigned with single, double, triple single/double quotes

#Hints

#Numeric Types
#int type

#float type

#exponential


#Misc Types
#bool types: used for performing logical and conditional operations

# complex numbers:

#None -

#bytes - used for converting the values to byte/binary format before transfer across the network or for processing in a secured fashion

#Complex types - list, tuples, set, dict we learn later

print('G. Operators')
#Python supports operators -> assignment, arithmatic, comparison/relational, logical,
# unary (least priority), binary (least priority), ternary (least priority), bitwise (least priority)

#Assignment Operators ()- used to assign some values to a variable - return the value/reference as a result


#Arithmatic Operators () - will returns operated value as a result


#Relational operators () - Used for comparing variables and values and returns boolean type as a result


#Logical Operators () - apply logic between multiple output of the relational operators and Returns boolean
#or -

#and -

#not -

#Bitwise Operators (&, |) - same like logical operator (Costly to use) -

#Unary

#Binary

#Ternary

#One program covers almost all these operators

###########One Reallife usecase program to bring all types of operators in one Program###########
#Swiggy food purchase -> coupon max discount of 100 or 10% which ever is lesser


print('J. Conditional Structure')

#I can/must/minimum have if condition alone -
#I must have if condition with else statement -
#I can have only else if or else statement -
#I can have if condition with else condition alone -
#I can have if condition with else if condition alone -
#I must have if condition with else if condition and else statement also -
#I should have my conditional structure started with if (if should be used only once),
# but can have multiple elif and should have only one else

#Minimal Conditional Structure

#Conditional Structure with multiple condition

#Nested conditional structure, which has to be used appropriately, needs lot of iterative testing


#Quick Usecases:
#Usecase1: Find the greatest of 2 and then 3 numbers using built in functions (max(list of values))

#Usecase2:
# "if" user clicked on the popup then provide the options available upcoming batch or ask anything
# "if" user choosen upcoming batch -> ask user to choose either de or ds or cloud or devops else inform course is not available
# "if" user choosen ask anything ->

print('J. Looping Constructs')
#Looping Construct concepts ->
'''
Category -> 
Conditional looping (entry & exit) eg. while i<=j or while True (do while loop) 
Un Conditional looping - for loop
Types (for, while + do while - not available directly in python (rather we use while True (exit controlled)))
break -> break will terminate the iteration of a loop and come out of the loop 
& continue -> continue will skip the iteration of a loop and continue to the next iteration
'''
#Iteration or repetitive execution of the some tasks across data or programs is called loops
#Two way of Performing Looping - Conditional & UnConditional loopings

#for loop is an unconditional looping


#A Realtime Example of for loop on a list of salary (Unconditional Looping)


#while loop is a conditional looping


#Realtime example of a conditional looping


#Let's try to understand the looping concept in detail with some case studies including the other constructs like break and continue:
#First lets' learn For loop -
#For loop will run on an iterable type only
#For loop is a unconditional looping
#For loop - number of iterations are already known


#How to write a simple for loop


#Nested For loop
#I wanted to calculate bonus applied salary


#for empname,sal in emp_lst,sal_lst:#We can't iterate on more than one list using a single looping construct
#    print(f"bonus applied salary for {empname} is ",int(sal+(sal*(bonus_percent/100))))
#This below approach for finding empname and the salary of the given employee, will not work as we expected


#Let's try with Nested looping: The below nested looping will not work


#Let's try with Nested looping: Using an important function called "enumerate" we can get the index also with the element and apply in other list


#When Do we use Nested For loop
#An University wanted to provide the subjects to all affliated colleges



#For Loop with Break and Continue constructs/clauses:
#Break is used to break the execution of the loop by come out of the loop if a given condition matches
#Continue is used to skip the given iteration of the loop (and execute the next iteration) if a given condition matches


#Let's fine tune the above looping construct to only iterate the required number of times
# (3 times only rather than 5 times)
#The loop will run only 5+1 times


#Break is only effective if we sort the data?
#exists in sql's


#continue construct: continue will help skip the current iteration and continue with the next iteration


#Usecase1: Try create tables for your kids from 2 to how many tables (get as an input)?
# using simple or nested for loop, skip the 5 and 10 tables
#Table has to created upto 12 numbers


#While Loop

#Looping constructs available in Common Prog languages - for, while and do while
#Looping constructs available in Python language - for and while (no do while is available in python)
#Types of Looping - Entry Control & Exit Control loops


#All about While loop:
#
#
#


#How to create infinate loop using while to run some process/operation continuously
#In the other hand if we don't manage the conditions properly, it will leads to infinate looping


#Convert the for loop into while loop - conclude which is better to use for iterating list of values? FOR LOOP is considerable


#Realtime Example of using While loop: Entry controlled loop
#Login username/password used in our routine life
# username=input("User name\n")
# storedpasswd="hduser"
# attempts=1
# maxattempts=3


#Usecase2 related to exit controlled loop (do while loop) + break & continue:
#Create a scheduler program to run a code minimum once or continue to run multiple hours + skipping odd hours
#eg. sfm_insure.py (some print statement)

##############################################Condition Structure & Looping Constructs####################################

print('K. Collection Types')
#Application of using collection types in realtime world?
#Self served metadata driven Data movement automation (DMA) tool
#{"process":"ETL Process1","source":["hive","Bigquery"],"target":["HDFS","GCS"],"cols":["custid","upper(custname) as upper_custname"],"tablename":"customer","where":"(city='chennai')","gcs_uri":"gcs://abc/xyz_bucket/"}


#Hive -
#Python -

#What is a collection type?

#Examples of Collection Types:

#list


#dictionary


#tuple


#set


#Notataions:

#Example of all collection types used:
#{'process': 'ETL Process1', 'source': {'hive', 'Bigquery'}, 'target': ['HDFS', 'GCS'], 'cols': ['custid', 'upper(custname) as upper_custname'], 'tablename': 'customer', 'where': "(city='chennai')", 'uris': ('gcs://abc/xyz_bucket/', 100)}

#Different types of collection types? in the order of importance
#list, dict, tuple, set

#Why we need collection types?
#To manage/store/parse the complex dataset in a hirarchical/nested/complex structure stored or to process semi structure data, nested data,
# dynamic schema-ful data (avro), variable data/metadata, for a data or metadata driven approaches..

#Different characteristics of collection types?
#Iterable (looping), mutable (changable) - updatable (modifyable) & resizable (added/removed), accessible (select using index, position, value, key)

######What are the topics we have to learn in collection types#######
#Iterable? Yes, all collection types are iterable in python.

#Notation, access, resizable/mutable/immutable?  insert/update/delete, functions to apply
#All the above we are going to see in detail
#Notation:
#Accessed using ?
#Definition: Indexed, sequenced collection of homogeneous elements

print("list operations")
#List can be hetrogeneous too (but not suggested, why ? because while operate between the elements of the list, program fails because python is a strongly typed language)


#All the python collections are iterable -


#select/access


#insert/update/delete (list is mutable, hence updating and resizing (add/removing) is possible)

#append in the last (proves list is mutable/resizable/can be inserted)


#insert in the index position


#update the list elements (mutable)

#delete the elements of the list using value


#delete multiple same elements using the value


#pop (delete) the elements of the list using index


print("list after popping out a given index element")

#search for a value with in the given index (range) value and pop(remove) it




#Wanted to remove the duplicate in a given list?
#Convert to set and back to list

#certain builtin functions to try out on list




print("Dictionaries (mutable) - {k:v, k:v}")


#Access a dictionary - using key


#Adding Items - if the key is not found


#Updating Items - if the key is found


#Removing an Item (from the last)

#Delete(pop) the given key

#Delete all the elements of a dict
#dict1.clear()


#Iteration of Dictionary
#Iterate on the items of the Dict - will return what datatype???tuple


#Iterate on the keys of the Dict - will return what datatype???respective key's datatype


#Iterate on the values of the Dict - will return what datatype???respective value's datatype

#Some additional functions

#Setdefault will add the key and value provided if key is not present already, if already present consider the given value and not the default value

#create a dictionary with the keys from list and value from the second argument


print("Tuples (immutable?)")
#Definition of Tuple:Tuple is an indexed sequenced collection of hetrogeneous elements, tuples are immutable (non updatable and non resizable)
#Notation is ()


#select/access
#City where Anirudh present

#count of some element in the given tuple

#search for some element in the given tuple to identify the index


#Resizable? No (insert/delete)
#Try to Add some elements to the tuple, lets try to add age of Anirudh
#Insert/Append? No


#delete? No
#tup1.__delattr__(name="Chennai") #cannot delete the elements of tuple

#Modify (update) - Not possible


#I want to achieve Insert/update/Delete in a tuple? Not possible by default,
# but we can do some workaround to achieve it? convert to list , do insert update delete and convert back to tuple

#Do all operations/functions that list supports (#Other functions to apply)
#Insert


#Update

#Delete


#Convert the list back to tuple



print("Set (mutable) (least important)- Notation {} - "
      "Set is a sorted and distinct collection of iterable elements, cannot be accessed using index ?? Why?")

#how to access the element of a set (cant be access directly by using index/key/values)- Index can't be used why?
#The number of elements/items in the set is not fixed in the numbers or sort order
#set1[0] #not possible to access using index

#set is iterable?yes


#set is mutable?Yes
#add will help add/update an element not the set

#update will help add/update another set


#set is mutable (resizable) - Removing/popping/cleaning


#set is supported with set operation (If we use set, we use it for these purposes)
#Requirement of identifying the common department in the given lists

#intersect - combine both the sets


#difference (difference/subtract/minus) - find the difference between the sets

