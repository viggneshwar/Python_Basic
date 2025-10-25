#Refer python_theory/notes for understanding few basics of python...
'''
What we are going to learn in Python???
**1. Basic programming fundamentals -
A. Intent/Block based coding
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
'''
How to uninstall/install pip packages.
python -m pip freeze
python -m pip uninstall pandas
python -m pip install pandas==2.3.1
'''
print("************** 1. Basics of Python Programing*************")
print("How to run a python program")
#right click this module tab and run the program or go to run menu and run or click on the play button in the right top
#or type ctrl+shift+f10

#Day1:15/10/2025
#Fundamentals of Python Programming:
####################################
print("A. Python is an indent based programming language")
#Why Python uses indend based programing ->
#1. Managing the program more efficiently
#2. Better Readablility of the code
#3. For creating the hierarchy of programming.
#4. By default 4 spaces we will give for indends, but more/less spaces or tabs also can be used...

#Indendation is needed for (hierarchy of programming),
# because we are doing block operation (lines of code) with in the for loop
team=['wd36','we47']
for i in team:
    print(f"hello {i} Team")
    print("thank you")

#Linux is not an intend based program, it is a block based rather:
'''
for i in `ls` 
do #starting a block
 echo "listing files in the folder"
    echo $i
echo "Thanks"
done #Ending the block
        echo "Completed"
'''

#indendation has to be uniform within the block of code (not mandatory across the block of code)
#below prog doesnt work if we are using different number of spaces between lines of code in a given block
for i in range(1,4):
    print("inside i")
    print(i)
    for  j in range(1,2):
      print("inside i")
      print(j)

#optimal number of spaces has to be 4, but any numbers you can give, dont use both tab & spaces

print("B. This is a commented line in Python")
# What is comment? Comment is a info/description/additional information for better understanding,
# which will not affect the program execution
# Usage of Comments: For descriptive purpose & for creating dead codes
#Comments are of 2 types:
# 1. Single line - #
# 2. Multi line or block comments - '''  '''
#print("hello is commented") #single line comment
'''
for i in range(1,4):
    print("inside i")
    print(i)
'''
#Comment is used as description too...
def abcd():
    '''This is a function to do something'''
    for i in range(1, 4):#this for loop is going to iterate 3 times from 1 to 3
        #print("inside i")
        print(i)#printing the value of i in every iteration

print("C. Playing with Quotes: Python treats single quotes the same as double quotes as like triple quotes, but has some differences")
#Python treats single quotes the same as double quotes and triple quotes.
var1='Inceptez'
var2="Inceptez"
var3="""Inceptez"""
print(var1,var2,var3)

##we can use escape sequence also - \ is used to tell python not to consider the following content of \
print('This is an Inceptez\'s property')

#Single quotes example
var1='This is an Inceptez property'

#Double quotes is used for holding single quoted chars
#var2='This is an Inceptez's property' #this is not runnable
var2="This is an Inceptez's property"

#var_with_both_single_double_quotes="This is an "Inceptez's" property" #this is not runnable

#Triple quotes:
#Triple quotes can handle multiple quotes like single or double or any other characters
var_with_both_single_double_quotes="""This is an "Inceptez's" property"""
#Triple double quotes is used for muliline
#For handling paragraph/multilines text, we can use 3 single or doublequotes
var_with_multi_line="""Hi Team,
Good morning"""

#Any programming language learning has to be started first learning about variables
print("D. Let's learn all about VARIABLES")
'''1. Variable Properties - Dynamic Inference, Dynamic Typed, Strongly Typed'''

#Dynamic inference - based on the assigned value to a variable, it will automatically decides/infer/identify/refers the data type dynamically
age=43
print(type(age))
height=5.11
print(type(height))

#Dynamically typed: If a variable is created with a specific data type, can be changed later by performing soe eration
amt=100
print(type(amt))
#<class 'int'>

#below is possible, because python is dynamically typed language (Duck type language)
amt=amt+(amt*.1)
print(type(amt))
#<class 'float'>

'''Scala is a statically typed language
scala> amt=100
scala> amt
val res0: Int = 100
 
#below is not possible - because of statically type feature
scala> amt=amt+(amt*.1)
           ^
       error: type mismatch;
        found   : Int
        required: ?{def +(x$1: ? >: Double): ?}
'''

#Strongly typed: Python allow us to operate between the variables of Similar datatype (of the same hierarchy) and doesn't allow to operate between different datatypes.
name='irfan'
amt=100
#print(name+amt)#this fails
#TypeError: can only concatenate str (not "int") to str

#Overcome this property by using type conversion functions
stramt=str(amt)
print(name+stramt)

#Scala is Weakly typed language: Allow us to operate between the variables of Any datatype
'''
scala> var a=10
var a: Int = 10
scala> var b="Inceptez"
var b: String = Inceptez
scala> b+a
val res1: String = Inceptez10
'''

print("E. Naming Conventions")

#MohamedIrfanKader - Pascal/initcap case
#mohamedIrfanKader - Camel case (methods/functions)
#mohamed_irfan_kader - Snake case (n_n_n_)
#MOHAMEDIRFAN - upper case
#mohamedirfan - lower case

#A variable can have camel case or init upper or with underscores snake case
total_number_of_aspirants=69
totalNumberOfAspirants=69

#A variable name must start with a letter or the underscore character
fullName="Inceptez Technologies"
full_name="Inceptez Technologies"
_revenue=1000000#protected for broader group, open for smaller group
__profit=100000#private for intented group

#A variable name cannot start with a number
fullname1="Inceptez Technologies"
fullname2="Inceptez Technologies Pvt Ltd"

#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
full_name_123='inceptez technologies'

#Variable names are case-sensitive
abc=10
Abc=20
ABC=30
print(abc,Abc,ABC)

#Multiple Variables can be assigned in a single line (Multi Assignment)
name,age,city="Irfan",43,"Chennai"
print(name,age,city)

#Variable name should not be a reserved keyword
len1=len(name)#This is not a right naming convention to use

print("F. Type identification & Casting")
#Functions we are learning in this topic (type, isinstance, casting(int,str,float etc.,))
#What we are learning here is the usage of few functions like type, isinstance, casting functions
age=43
#To understand/identify the age is of what type
print(type(age))

#To check wheter the age is of an expected type
age=43
print(isinstance(age,int)) #True
age='43'
print(isinstance(age,int)) #False

#To convert the age to an expected type
age=int(age)
print(type(age))
age=43
age_float=float(age)
print(type(age_float))
age_str=str(age)
print(type(age_str))
#Check for a given type, if it is not as expected then cast it to the expected type programatically using if condition

print("G. Standard Input & output options")
#assigning value statically/hardcoded
name='irfan'
age=input("enter your age")
#any function that we use may have input &/ output arguments/results

#assigning value dynamically using the function called input()
#Default Characteristics this input function has:
#Character1: input will take the input value interactively with the default type of string
#Character2: input will take the input without prompting with anything, but we can add the prompt with some content
name=input()#input without any prompt (character2)
print(type(name))#str (character1)

age=input("enter the age: ")#input with a meaningful prompt (changing the character2)
print(type(age))#str (character1)

#Better to use
age=int(input("enter the age: "))#input with a meaningful prompt (changing the character2) and typecasting input output to integer (changing chararcter1)
print(type(age))#int (character1 changes)


#print statement will be used as a std output function
print("hello")

#semi colon can be used to seperate a statment if we write multiple statements in one line

#below print function is taking only 1 argument (but print can take any number of arguments)
print("good morning team")#one input one output
#below print function is taking multiple arguments and printing them individually as multiple output
name='inceptez'
age=11
print("name of the company",name,"age of the company",age)#4 input and 4 individual output seperated with space

#Formatted string Print statements - positional formatting args - not much important
name='inceptez'
age=11
#Positional arguments
print("name of the company name age of the company age")#1 input and 1 output
#drawback is the above print with print even variable name as a value, not the actual value...
#to overcome, we have a concept of format function...
print("name of the company {0} age of the company {1}".format(name,age))#positional formatting arguments

#keyword/named formatting arguments - not much important
print("name of the company {n} age of the company {a}".format(n=name,a=age))#named formatting arguments

#Formatted string Print statements other way (3x onwards) - named args - important and advance and simple
print(f"name of the company {name} age of the company {age}")

print("H. Datatypes, Mutability & Builtin Functions (later)")
#Simple Types: string, numeric (int, float, complex), misc
#Complex or Collection Types: list, dict, tuple, set
#Simple Type (Sequence Type) -
#string type -
# Definition: Indexed sequenced collection of characters
#eg. name='inceptez'
#01234567 Indexed sequenced collection of chars
#inceptez
# can be assigned with single, double, triple single/double quotes
name='inceptez'
name1="inceptez"
name2="""inceptez"""

#Hints - hints in python is used to identify the type easily or descriptively
name3:str='irfan'
age1:int='43'#This is still a string, the :int is for just descriptive or hinting purpose
print(type(age1))#string
age2:int=int('43')
print(type(age2))#integer

#application of hint
def bonus_calc(sal:int,bon:float):
    return sal+(sal*bon)#Dynamic typing character

print(bonus_calc(100000,.20))
#Immutability - non changable
company_name='inceptez'
#company_name[0]='I' #Item assignments/modification in a string is not possible because of immutability

#Numeric Types (int, float, complex)
#int type - single whole number, it is non indexed/sequenced, it is immutable (non modifiable)
age=43
age_hint:int=43
'''
age[0]=5#will not work because int is immutable
print(age[0])#will not work because it is non indexed
for i in age:#will not work because it is non sequenced
   print(i)
'''
#float type: single decimal number with scale and precision, it is non indexed/sequenced, it is immutable (non modifiable)
height=5.11#5 is the scale and 11 is the precision
height_hint:float=5.11
#as like integer, float also is immutable, non indexed and non sequenced

# complex numbers: Contains the real and imaginary part in a format of 10.5j (where is 10 is real and 5j is imaginary)
#especially used in the scientific, electrical, data science environments, applied maths (ensemble model).
complextype=complex(5.11)
complexvalue=5.10+2j
print("real value is",complexvalue.real)
print("imaginary value is",complexvalue.imag)
print("conjugate of complex value",complexvalue.conjugate())

#Misc Types (bool, none, exp, bytes)
#bool types: Boolean is a true or false return value of operations we performed
boolout:bool=1>2
print(boolout)#return boolean of false
print(1<2)#return boolean of true

#None types: It is a type represents the value is not available
a=None
#print is a function that return none
type(print())

def a():
    print("hello team")
    #return 'something' #If i dont have return then it will return none

#exponential - Exponent of 0's
#1.5j #complex number
exponential_value=2e3 #exponents e3 means 10 to the exponent of 3 = 10*10*10 = 1000
#result 2000

#bytes - used for converting the values to byte/binary format before transfer across the network or for processing in a secured fashion
byte_a=bytes(100)#Converting a number to a bytes type before tranfering across the network...
print(type(byte_a))
print(byte_a.decode('utf-8'))

#Complex/Collection types - list, dict, tuples, set we learn later

print('G. Operators')
#Python supports operators -> assignment, arithmatic, comparison/relational, logical,
# unary (least priority), binary (least priority), ternary (least priority), bitwise (least priority)

#Assignment Operators (= or += or -=)- used to assign some values to a variable - return the value/reference as a result
age=43#here variable age is assigned with a value of 43
age+=1#here variable age is assigned with a value of 43+1 (value is operated with an arithmetic operator)
#or
age=age+1#here variable age is assigned with a value of 43+1 (value is operated with an arithmetic operator)
name=name.capitalize()#Here i am assigning the result of a function as a value to the name variable
i=int#i is a variable referring a program called int
#conclusion is an assignment operator can be used to assign a value or refer a program

#Arithmatic Operators (*/+- ** % ()) - will returns operated value as a result
#BODMAS rule (Precedence order -> Brackets, Orders (exponent/sqrt), Division or Mul, Add or  Sub
mul=5*10
div=10/2
add=100+200
sub=100-200

final_res=100+200/100-200#without using BODMAS
final_res=(100+200)/(100-200)#using BODMAS

power_val=2**4#2 to the power of 4 ie 16
mod_val=10%3 #Result is 1

#Relational operators (==, !=, >, <, <=, >=) - Used for comparing variables and values and returns boolean type as a result
print(5!=10)
print(5==10)
result:bool=5==10#We are assigning and comparing
print(result)
print(type(result))

#Logical Operators () - apply logic between multiple output of the relational operators and Returns boolean
#or - will check for the first occurance of true and return true
print("this will just print true once 1==1 is identified, it wont got to 3==4 check",1==1 or 3==4)

#and - will check for the first occurance of false and return false
print("this will print false after validating 1==1 and 3==4",1==1 and 3==4)
print("this will just print false after validating 3==4, it wont validate 1==1",3==4 and 1==1)

#not - It is negation/opposite of the and and or result
x=not(True)#return False
y=not(False)#return True
print(x,y)
print("this will print false after validating 1==1 and 3==4",not(1==1 and 3==4))

#Least bother, but know about these operators once for all...
#Unary (-) = an operator used to identify the sign of a value assigned
bank_balance=-10000
tax=-.18
gross_sal=100000+10000
print(f"final salary {gross_sal+(gross_sal*tax)}")

#Binary - If I operate between 2 or more variables/values using an operand
a=100
b=200
print(a+b)#binary operator example

#Ternary - Short form of using the operators to achieve SIMPLE conditional/looping outputs in a
# single line short form
#Typical control (conditional) structure
if a<b:
    print("true output of a is lesser")
else:
    print("false output of b is lesser")

#Ternary - above conditional structure can be writterned using the ternary operator in a single line short form
#Ternary operator breaks the rule of indent and block based programming, we will write all simple functionality in one line
print("true output of a is lesser",a) if a<b else print("false output of b is lesser")


print('J. Conditional Structure')

#I may/must have if condition minimum - must
#I must have if condition with else statement - false (may)
#I can have only elif or else statement - false (if is mandatory)
#I can have if condition with else condition alone - true
#I can have if condition with elif condition alone - true
#I may have if condition with else if condition and else statement also - true
#I should have my conditional structure started with if - True
#if should be used only once in a conditional structure - False (we can use nested if)
# We can have multiple elif and should have only one else in a given block (not nested) - True
#signature of if is completed with colon (:)

#Minimal Conditional Structure
#simple example
if True:#use either or both relational or logical operators to get boolean
    print("execute the if block code...")

#Conditional Structure with multiple conditions (if and elif)
if 0>1:
    print("execute if block code...")
elif 2>1:
    print("execute first elif block code...")
elif 3>2:
    print("execute second elif block code...")

#Conditional Structure with multiple conditions and unconditional also (if and elif and else)
if 0>1:
    print("execute if block code...")
elif 2>3:
    print("execute first elif block code...")
elif 2>4:
    print("execute second elif block code...")
else:
    print("None of the above conditions are met")

#Nested conditional structure, which has to be used appropriately, needs lot of iterative testing
if 0>1:
    print("execute if block code...")
    if True:
        print("execute nested if block code in the if block...")
elif 2>3:
    print("execute first elif block code...")
elif 2>4:
    print("execute second elif block code...")
else:
    print("None of the above conditions are met")

#Reallife example of nested if
time=9.30
month='october'
if month=='october':
    if (time > 9 and time <= 10) or (time >= 6.30 and time < 7):
        print("Restarting the zoom for one on one video connect")
    else:
        print("it is a different time >10 or <6.30")

#Quick Usecases:
#Usecase1: Find the greatest of 2 and then 3 numbers not by using built in functions


#Usecase2: Pseudo code
# "if" user clicked on the popup then provide the options available upcoming batch or ask anything
# "if" user choosen upcoming batch -> ask user to choose either de or ds or cloud or devops else inform course is not available
# "if" user choosen ask anything ->
# "if" user clicked on the popup then provide the options available upcoming batch or ask anything
popup=True
if popup:
    print("choose either up bat or ask anything")
    tab_clicked=input("choose either up bat or ask anything")
    if tab_clicked=='up bat':
        course_interested=input("choose de or ds or cloud or devops")
        if course_interested=='de':
            print("Data engineering course has been chosen","weekday  7 to 9","weekend 9 to 1.30")
        if course_interested=='ds':
            print("Data science course has been chosen","weekend 9 to 1.30")
    elif tab_clicked=='ask anything':
        print("provide your question, we will get back to you")
        msg=input()
        #msg wil be mailed to inceptez team
else:
    print("other page clicks happened")

#CASE WHEN Suspicious THEN 'FLAGGED' ELSE 'NORMAL' END
'''
if suspicious:
   transaction_flag="flagged"
   print("flagged")
else:
   transaction_flag="normal"
   print("normal")   
'''

#Usecase3:
#One program covers almost all these concepts including operators
###########One Reallife usecase program to bring all types of operators in one Program###########
#Swiggy food purchase -> coupon max discount of 100 or 10% which ever is lesser
total_cart_amt=int(input("enter total cart amount"))
offer_disc_pct=.10
offer_max_amout=-100


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

