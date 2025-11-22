#Refer python_theory pdf/notes for understanding few basics of python...
'''
What we are going to learn in Python???
**1. Basic programming fundamentals -
A. Intent Block based coding
B. Comments
C. Quotes
D. Variables & Values
E. Naming Conventions

F. Types (Simple) and Casting
G. Input & Output operations
H. Datatypes (Simple/premetive or Complex/Collection (data structure))

I. Operators
J. Conditional Structure
K. Looping Constructs
L. Complex/Collection Types (Data structure) 2d to 3d


#Specific to Python (next level) 2 weeks
2. Exception Handling - Basics
3. **FBP - Dataengineers (eg. leverage the spark functions writtern by somebody)
4. OOPS - Framework developers (eg. commiters/contributors of apache spark)
5. Building Apps/APIs/AI integration using Python Programming + AI Integration...

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

print("E. Naming Conventions - package, module, class, object, method, variable")
#A variable can have camel case or (init upper or pascal) or with underscores/snake case
ourCompanyName='Inceptez'#camel case
our_company_name='Inceptez'#snake case
OurCompanyName='Inceptez'#pascal case/init upper

#A variable name must start with a letter or the underscore character
name='irfan'
_name='irfan'
name1='inceptez'
#-name

#A variable name cannot start with a number
#1name

#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
My_123_name='irfan'

#Variable names are case-sensitive
name='irfan'
Name='Inceptez'
print("both are different variables because of case sensitiveness",name,Name)

#Multiple Variables can be assigned in a single line (Multi Assignment)
name,Name,NAME='irfan','inceptez','bharathi'
print(name,Name,NAME)

#We should not use the name of a program or variable which is already a reserved one.
'''
len=10#we shouldnt do this, because len is a built in function, which will be overrided with 10
'''

print("F.Types & Casting")

#3. How to check a given TYPE is of what datatype we expect  & type casting
#Functions we are learning in this topic (type,str/int/float(),isinstance())
#What we are learning here is the usage of few functions like
age=43
#To understand the age is of what type
print(type(age))

#To check whether the age is of an expected type
print(isinstance(age,int))#True
print(isinstance(age,float))#False

#To convert the age to an expected type
age=str(age)
print(age)
print(type(age))

#Check for a given type, if it is not as expected then cast it to the expected type programatically using if condition
age=int(input("provide your age"))
if isinstance(age,str):
    print("age is already of type string, nothing to do here")
else:
    print(type(age))
    print("age is of above type, I am explicitly converting to string")
    age=str(age)

print("G. Standard Input input() & output print() options")
#assigning value statically
age=43
name='irfan'

#assigning value dynamically using input() - input will take the input using keyboard via console
#few characteristics of input function-
# a. if we dont prompt, then blank space is prompted
# b. input will return by default every input as string type
age=int(input("enter your age"))
name=input("enter your name")
print("name of the person is ",name,"age of the person is",age)

#print statement will be used as a standard/console output function
#In general in python, semi colon can be used to seperate a statment if we write multiple statements in one line
print("hello"); print("gm"); print("good evening")
a=10;b=20;c=30
print(a,b,c)

#below print function is taking only 1 argument (but print can take any number of arguments)
print("good morning team, we are learning python basics")#only 1 argument
#below print function is taking multiple arguments and printing them individually
print("good morning team","we are learning python basics")#only 2 arguments
print("good morning team","we are learning python basics",sep='-----')#only 2 arguments

#Formatted string Print statements - positional args
#Formatted string Print statements other way (3x onwards) - named args
print("name of the person is ",name,"age of the person is",age)
print("name of the person is name and age of the person is age")#it will not print the output formatted with the values, rather names will be printed
print(f"name of the person is {name} and age of the person is {age}")#important to know
var1=f"name of the person is {name} and age of the person is {age}"
print(var1)
#Positional arguments (least bother)
name='inceptez'
age=11
print("name of the person is {0} and age of the person is {1}".format(name,age))
#keyword/named arguments (least bother)
name='inceptez'
age=11
print("name of the person is {nm} and age of the person is {ag}".format(nm=name,ag=age))

print("H. Datatypes (important),  Mutability (later) & Builtin Functions (later)")

#Types of data types - Simple & Complex/Collection & Misc types
#Python doesn't contains a rich collection of data types as like other languages
#Simple type
    #Numeric (int,float,complex)
    #String (str)
#Misc (None, Bool, exp, bin, bytes)
#Collection (list, dict, tuple, set) - we learn later as a seperate topic (data structure)

#Hint in variables/functions (giving a hint of a variable for a better understanding, and it won't affect the type)
height1:float=input("enter height in cms")#this float is just a hint

def area(height:int,width:float):
    return height * width
print(area(10,20.0))

#Numeric Types
#int type
age=43
print(type(age))
#float type
height=5.11
print(type(height))

#Complex (least bother) # it is not used in general, other than mathematical and logistical equations
graph_axis=10.1+3j#complex data with real and imaginary values kept together
print(type(graph_axis))
print(graph_axis.real)
print(type(graph_axis.real))
print(graph_axis.imag)
print(type(graph_axis.imag))

#exponential operator returns float type
#3e2 will work like 3*(10.0*10.0) or put 2 zeros after 3
emp_cnt=3e2#employees count exponentially increased from 3 to 300
cluster_node=3e2#inceptez is exponentially increasing the number of nodes in their cluster from 3 to 300

#Sequence Types
#string type -
# indexed sequenced collection of characters
# can be assigned with single, double, triple single/double quotes
#name=01234567#indexed and sequenced
name='inceptez'
print(name[0])#print i
print(name[1])#print n

#string is immutable type
#name[0]='I' This will not work, because string is immutable...

#Misc Types
#bool types: used for performing logical and conditional operations
active_flag=True
print(active_flag)
print(type(active_flag))
active_flag=False
print(active_flag)
print(type(active_flag))


#None - Unassigned or unavailable (equivalent to null in database)
profession=''#profession is intentionally given as blank because he is not working currently
profession=None#profession is not given intentionally by the customer
result_of_print:None=print(profession)#print will just print something in the console, it will not return anything

#bytes (least bother) - used for converting the values to byte/binary format before transfer across the network or for processing in a secured fashion
a=100
print(bytes(a))

#binary
a=5
print(bin(a))

#Collection/complex types - list, tuples, set, dict we learn later

print('G. Operators')
#All operators in one line for a quick reference (not a meaningful expression we wrote)
a=not(a!=b+b) | -5+6 if 1==1 else 1
#assignment : a=
#comparison/relational : a!=b
#arithmetic : b+b
#logical : not(a!=b+b)
#bitwise : |
#unary : -5
#binary: -5+6
#ternary: -5+6 if 1==1 else 1

#Python supports operators -> assignment, arithmatic, comparison/relational, logical,
# unary (least priority), binary (least priority), ternary (least priority), bitwise (least priority)

#Assignment Operators ()- used to assign some values to a variable - return the value/reference as a result
age=43
age+=1#my age is increased to 44

#Arithmatic Operators (+-*/ ** e //) - will returns operated value as a result
age=43
age+1
print("my age is increased to ",age+1)
aspirant_cnt=59
#after 1 pm
aspirant_cnt=aspirant_cnt-10
print(5*2)
print(59/30)
print(59//30)#floor division to avoid fraction value
print("power of 2",15**2)
print((59/30).__ceil__())

#Relational operators (==,<=,>=,>,<,!=) - Used for comparing variables and values and returns boolean type as a result
print(5>3)#return boolean
print(5==3)#return boolean
print(5>=3)#gt or equals return boolean
print(5<=3)#lt or equals  return boolean
print(5!=3)#not equals  return boolean

#Logical Operators () - apply logic between multiple output of the relational operators and Returns boolean
#or - Returns the first true output
print(False or True or False)#returns True
#and - Returns the first false output
print(True and True and False)#returns False
#not - Returns the negation/opposite of the boolean output
print(not(True and True and False))#returns not(False)=True

#Note:We understood brackets place a vital role in the result...
print("Output of this expression is True or (True and False) => True or False => True",5>3 or 4>3 and 5>5)
print("Output of this expression is (True or True) and False => True and False => False",(5>3 or 4>3) and 5>5)
print("To ensure use brackets appropriately for sure - Output of this expression is True or (True and False) => True or False => True",5>3 or (4>3 and 5>5))

#BODMAS Rule: Priority - Brackets, Orders (power/exponents), Division/Multiplication, Add/Sub
a=10+3*5**2/5-3
'''>>> 
a=10+3*5**2/5-3
>>> a
22.0#result
>>> 5**2     #orders 
25
>>> 25/5 #Division
5.0
>>> 25/5*3 #Multiplication
15.0
>>> 10+15.0 #Addition
25.0
>>> 10+15.0-3 #Subraction
22.0
'''
'''
We overrided the bodmas rule using brackets 
a=(((10+3)*5)**2)/(5-3) #B A M O S D
'''

#Least bother about the below items, just know once for all....
#Bitwise Operators (^, &, |) - same like logical operator (Costly to understand)
print(5 | 7)#7
'''
bin(5)
'0b101'
bin(7)
'0b111'
101 | 111 => 111 (7)
101 & 111 => 101 (5)
'''

#Unary
curr_temp=-10 #An assignment we do with a signed value in an operand (operand that has the operator also integrated)
#Binary # operator that performs operation between (2 operands) more than 1 operand
sal=100000
bon=10000
total_sal=sal+bon

#Ternary Operator : It breaks the rule of writing simple conditional structure as an operator not as a block with intent
#Ternary operator allow us to write the conditional structure with single line of block of code
print("true") if True else print("false")#This is ternary operator

print(f"you may be a higher exp candidate {10+20}") if sal>90000 and sal<1000000 else print("lower salary")


#Conditional Structure (it is a block of code with proper indentation maintained)
if sal>90000:#if block, following line 463 to 468 is the body of if
    print("higher salary")
    print("you may be a higher exp candidate")
    if True:#nested conditional structure(if we have a condition inside another condition)
        print("inside the nested if")
    else:
        print("inside the nested else")
else:#else block
    print("lower salary")
    print("you may be a lower exp candidate")

print('J. Control Structure ( Conditional Structure)')
'''
Syntax:
if conditions :
   body of the if
elif conditions:
   body of elif
else:
   body of else
'''
#Trip planner module
amt_hand=100
if amt_hand > 5000:#signature will be terminated with :
    print("plan  trip to Banglore from Chennai")#body of if
elif amt_hand > 2000:#signature
    print("plan  trip to mahabs from Chennai")  # body of else if
else:
    print("abort the plan")

#Rules while writing Conditional structure:
#Every conditional structure should starts with if condition : True
#Every conditional structure should contain either elif or else : False
if True:
    print("true")

#We can have inside if multiple other/nested conditions (if if if elif else) : True
if True:
    if True:
        if False:
            print("true")

#I can have if condition with else condition alone - True
if True:
    pass#I don't have any logic to write..
else:
    pass
#I can have if condition with else if condition alone - True
if True:
    pass
elif True:
    pass

#I must have if condition with else if condition and else statement also - True
#I should have my conditional structure started with if - True
#If should be used only once in a conditional structure - False
#In a conditional structure, I can have multiple elif and but should have only one else - True
if True:
    print("some logic i have writtened here")
    #pass#construct
elif True:
    pass
elif True:
    pass
elif True:
    pass
else:
    pass

#If can have either relational operator or/and logical operator in the signature - True
if 2>1 or 3>2:#if/elif condition should return either true or false by any way
    print("true")

#Minimal Conditional Structure
amt_hand=1000
if amt_hand > 500:
    print("plan for some movie")

#Conditional Structure with multiple condition in the if itself or using elif
amt_hand=1000
movie_ticket=True
bus_ticket=True
if amt_hand >= 500 and movie_ticket==True:
    print("plan for some movie")
elif amt_hand >= 1000 and bus_ticket==True:
    print("plan for a trip")
else:
    print("nothing to do")

#Nested conditional structure, which has to be used appropriately, needs lot of iterative testing
amt_hand=10000
bus=7000
train=6000
flight=6000
#Below program will check for the min eligible amout for starting the tour
#this program prioritize flight or train or bus
if amt_hand > 6000:#basic condition
    if flight <= train and flight <= bus:#nested condition
        if amt_hand >= flight:#not needed, since we checked this in the line 558 itself
            print("buy a flight ticket")
    elif train <= bus and train <= flight:
        if amt_hand >= train:
            print("buy a train ticket")
    elif bus <= train and bus <= flight:
        if amt_hand >= train:
            print("buy a bus ticket")
    else:
        print("flight ticket is costlier than train or bus")
else:
    print("no enough money to book any vehicle")

#Quick Usecases:
#Usecase1: Find the greatest of 2 and then 3 numbers
#Initialize variable (hardcode/dynamic input), ensure the type casting is done,
#Relational operator, logical operator, conditional structure / ternary operator
a=int(input("enter first value"))
b=int(input("enter second value"))
if a>b:
    print(f"a is greater, value of a is {a}")
elif b>a:
    print(f"b is greater, value of b is {b}")
else:
    print(f"both are same , value of a is {a} and value of b is {b}")

#ternary (complex to use)
print(f"a is greater, value of a is {a}") if a>b else print(f"b is greater, value of a is {b}") if b>a else print(f"both are same , value of a is {a} and value of b is {b}")

#Case statement in SQL is equivalent to if elif else ...
#CASE WHEN Suspicious THEN 'FLAGGED' ELSE 'NORMAL' END
trans="Suspecious"
if trans == "Suspecious":
    transaction_flag='FLAGGED'
else:
    transaction_flag = 'NORMAL'

#Can you try with 3 numbers comparison
a=int(input("enter first value"))
b=int(input("enter second value"))
c=int(input("enter third value"))
#regression: a==b==c, a>b & a>c, a==b or a==c and/or a!=c or a!=b
if a==b==c:
    print(f"all are same, value of a is {a}, value of b is {b}, value of c is {c}")
elif a>=b and a>=c:
    if a == b:
        print(f"a and b are same")
    elif a==c:
        print(f"a and c are same")
    else:
        print(f"a is greater, value of a is {a}")
elif b>=a and b>=c:
    if b == a:
        print(f"a and b are same")
    elif b==c:
        print(f"b and c are same")
    else:
        print(f"b is greater, value of a is {b}")
elif c>=a and c>=b:
    if c == a:
        print(f"a and c are same")
    elif c == b:
        print(f"b and c are same")
    else:
        print(f"c is greater, value of a is {c}")
else:#not needed, since the above >= will cover all the scenarios
    print(f"exceptional condition is met, check the value of a,b,c is {a} and {b} and {c}")

#Usecase2:
#pseudo code: pls extend this pseudo code as per the below program Bharathi have given
# "if" user clicked on the popup then provide the options available upcoming batch or ask anything
# "if" user choosen upcoming batch -> ask user to choose either de or ds or cloud or devops else inform course is not available
# "if" user choosen ask anything ->
def ask_anything():
    Question = input("enter your question")
    print("we will let you know the answer for your question",Question)

#website popup module
#pseudo code:
# "if" user clicked on the popup then provide the options available upcoming batch or ask anything
# "if" user choosen upcoming batch -> ask user to choose either de or ds or cloud or devops else inform course is not available
# "if" user choosen ask anything ->
popupclik=input("user click :yes/No")
if popupclik == "yes":
    print("available options:1.upcoming batches ,2.Ask anything")
    dropdown=input("choose your option")
    if dropdown == "upcoming classes":
        clasess=input("option courses 1.de,2.ds,3.cloud,4.devops:")
        if clasess=="de":
                print("you have selected de")
        if clasess=="ds":
                print("you have selected ds")
        if clasess=="cloud":
            print("you have selected cloud")
            check_ask_anything = int(input("choose 1.check timing, 2.ask anything"))
            if check_ask_anything == 1:
                print("Starting from 10 october, 2025")
            elif check_ask_anything == 2:
                ask_anything()
        if clasess=="devops":
                print("you have selected devops")
                check_ask_anything = int(input("choose 1.check timing, 2.ask anything"))
                if check_ask_anything == 1:
                    print("Starting from 8 April, 2025")
                elif check_ask_anything == 2:
                    ask_anything()
        if clasess not in ("de","ds","cloud","devops"):
                print("the course is not available")
    if dropdown == "ask anything":
        Question=input("enter your question")
        print("we will let you know")
else:
    print("No action taken")

#Usecase3:
###########One Reallife usecase program to bring all types of operators in one Program###########
#Swiggy food purchase -> coupon max discount of 100 or 10% which ever is lesser
#Get 10% discount using Bank of Baroda Debit Cards
#Maximum discount up to ₹100 (try this later: on orders above ₹499)
#Try to create this program using conditional structure basically
#Try to create this program by using all the concepts we learned so far... (tricky)

#Usecase3: strategic/smart
#One program covers almost all these concepts including operators and all the a to j
###########One Reallife usecase program to bring all types of operators in one Program###########
#Swiggy food purchase -> coupon max discount of 100 or 10% which ever is lesser
#Get 10% discount using RuPay Credit Cards Maximum discount up to ₹100 on orders above ₹600
#pseduo code:
'''Create a program to apply discount of 10% if the min amt is 600 and max cap of discount is 100 rupees
1.check for cart amt >= min cap amt else print the difference amout to add in the cart
2.Further check for the disc percent applied cart amt is exceeding offer max amt, then apply flat offer max amt
3.else check for the disc percent applied cart amt is not exceeding offer max amt, then apply disc percentage
'''
cart_amt=int(input("choose the food items to add in the cart, sum of amout will be considered"))
min_cap_amt=600#minimum amount company have defined
max_cap_discount=-100#unary operator
offer_pct=.10#snake case
if cart_amt > min_cap_amt or cart_amt == min_cap_amt:
    #pass #creating dead code
    #print("this transaction is eligible for the offer") #development i used this print, no more needed
    offer_amount=cart_amt*offer_pct#binary operator
    if offer_amount>=abs(max_cap_discount):#convert the max_cap_discount to positive integer
        final_discount_amt=cart_amt+max_cap_discount
        print(f"since the offer amount {offer_amount} is greater than the {abs(max_cap_discount)}, applying the flat offer of {abs(max_cap_discount)}, final amt is...",final_discount_amt)
    else:
        final_discount_amt=cart_amt-offer_amount
        print(
            f"since the offer amount {offer_amount} is less than the {abs(max_cap_discount)}, applying the offer percent of {offer_pct}, final amt is...",
            final_discount_amt)
else:
    print(f"Pls add this much amout in the cart to avail the offer {min_cap_amt-cart_amt}")

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
'''

print('K. Looping Constructs')
#Looping Construct concepts ->
'''
Category -> 
Conditional looping (entry & exit) eg.  
Un Conditional looping - for loop
Types ()
break ->  
& continue -> 
'''
#Control structure (conditional struct (if elif else), looping constructs ())
#What is a loop: Iterative or repetitive execution of similar tasks across different data or programs (with different input) is called looping
#What is basically a looping:
#drink water until your thirst is satisfied (conditional looping)
thirst=10
water_drinked=0
while water_drinked<=thirst:
    water_drinked=water_drinked+1
    print(f"drining water ", water_drinked)

#1.Categories of loops:
#Conditional looping (entry controlled (while) and exit controlled (do while))
#UnConditional looping (for loop) #important
#2. Names of looping:
#for and while loop, do while loop (python doesn't have do while loop)
#3. For controlling the flow of the loops, we can use the below statements:
#break & continue

#1.Categories of loops: for & while
######################All about For loop#######################################
#Lets first learn about Unconditional looping (for loop)...
#Characteristics of For Loop:
#For loop will run on an iterable type only (list, string, dict, tuple, set)
#For loop is a unconditional looping
# number of iterations are already known
#UnConditional looping (for loop) #important
#Example1:
lst_of_aspirants:list[str]=['gokula','mythili','mohan','divya']
for aspirant in lst_of_aspirants:#unconditional
    print(aspirant.upper())

lst_range=list(range(0,10))#I want to run a loop for 10 times to do something
print(lst_range)
for i in list(range(0,10)):
    print("hello")

#if i want to run a function 5 times once in 10 minutes
import time
for i in range(0,5):#[0,1,2,3,4]
    print('irfan'.capitalize())
    time.sleep(i)

#not advisable to create list of items manually, rather use range function
lst=[0,1,2,3,4]
for i in lst:
    print('irfan'.capitalize())
    time.sleep(1)

#for loop is an unconditional looping
#A Realtime Example of for loop (Unconditional Looping)
#If Inceptez has only 1 employee
#Example:
emp1_sal=50000
bonus=2000
print(f"bonus applied salary is {emp1_sal+bonus}")

#If Inceptez has 5 employees
emp2_sal=10000
bonus=2000
print(f"bonus applied salary is {emp2_sal+bonus}")
emp3_sal=10000
bonus=2000
print(f"bonus applied salary is {emp3_sal+bonus}")
emp4_sal=10000
bonus=2000
print(f"bonus applied salary is {emp4_sal+bonus}")
emp5_sal=10000
bonus=2000
print(f"bonus applied salary is {emp5_sal+bonus}")

#Better to place the salary in a list type and run a for loop to iterate on all salaries to give bonus
employees_sal=[50000,10000,10000,10000,10000]
bonus=2000
for emp_sal in employees_sal:
    print(f"bonus applied salary is {emp_sal + bonus}")

#dont consider this for now, just for making it perfect
employees_sal={1:[50000,10000],2:[10000,2000],3:[10000,2000],4:[10000,2000],5:[10000,2000]}
for empid,sal_bon_lst in employees_sal.items():
    print(f"bonus applied salary for employee id {empid} is {sal_bon_lst[0] + sal_bon_lst[1]}")

#Real Example of For loop:
#Usecase1: Try reading the data from our filesystem (accounts, branches, loan) and print the data in the screen
lst_of_files=['accounts.csv','branches.csv','loans.csv']
drive_location="C:\\dataset1\\"
#go to the terminal in pycharm alt+F12
#pip install pandas
import pandas
for file in lst_of_files:
    print(f"let me ask pandas to read first file from the {drive_location+file}")
    mem_table=pandas.read_csv(drive_location+file)
    print(mem_table.head(2))
######################All about For loop#######################################

######################All about While loop#######################################
#Characteristics of While Loop:
#While loop will run based on a condition because it is a conditional looping
#While is a conditional looping - number of iterations are not known already, it varies based on the incremental value and the condition used
#We have to use while loop causiously, if we miss the condition, it will run infinately...
a=10
b=1
while a>=b:
   print("hello",b)
   b=b+1#if we use the increment wrongly, then infinate loop will be formed...

#Conditional looping (while loop) #not much important as like for loop
#select * from tablename (for loop is running in the background)
#for row in tablecount:
#fetch row and print row
#example:
while 1==1 and False:#condition is needed that returns boolean (proves entry control loop)
    print("true")
    #break
#While is an Entry controlled loop : The loop will be executed by controlling the entry with the condition

starttime=9
endtime=14
while starttime<=endtime:#conditional, entry control loop
    print(f"run the session at {starttime}")
    starttime=starttime+1#incrementing one hour
else:
    print(f"sorry this is not the session time {starttime}")

#I wanted to rewrite/enrich the above program to engage the session only on weekdays or weekend?
#Using conditional structure and both looping construct in one program...
#Example2: Marrying unconditional & conditional looping with conditional structure (if condition)
#complete usage of the conditional structure and the looping constructs (for and while)
#Business requirement:
# Lets create a program to address both weekday and weekend team
#weekday team runs on monday to friday 7am to 9am
#weekday team runs on sat and sun 9am to 2pm
#What we learn in this one program is how to use the entire concept of control structures
#1. unconditional looping -  for loop
#2. conditional looping -  while loop
#3. conditional structure - if elif else
#4. nested control + conditional structure (under the control struct we can have conditional and vice versa too)
#Usecase:strategic/smart
trainer_input_batch=input("enter the batch name wd/we")
day_of_week=['mon','tue','wed','thu','fri','sat','sun']
for day in day_of_week:
    print("today is ",day)
    wd_st_time = 7
    wd_end_time = 9
    we_st_time = 9
    we_end_time = 14
    if (day =='sat' or day=='sun') and trainer_input_batch=='we':
        while we_end_time>=we_st_time:
            print(f"weekend run the session at {we_st_time}")
            we_st_time = we_st_time + 1  # incrementing one hour
    elif day not in ('sat', 'sun') and trainer_input_batch == 'wd':
        while wd_end_time >= wd_st_time:
            print(f"weekday run the session at {wd_st_time}")
            wd_st_time = wd_st_time + 1  # incrementing one hour
    else:
        print("no such batch or no session on this day")


#Conditional looping (entry controlled (while) and exit controlled (do while))

#do while loop (not directly available in python)

######################All about While loop#######################################

#Concept of Nested loops using for and while:
#Example1:
a=1
b=5
while a<=b:
    print("under while loop",a)
    for i in range(1,5):
        print("inside while and for",i)
    a+=1

#Nested While loop:
#Example2:
for i in range(1,5):
    a = 1
    b = 5
    print("under for loop", i)
    while a <= b:
        print("inside for and while",a)
        a+=1

#For a nested for loop we can take clock example
for hour in range(0,12):
    print("hour is ",hour)
    for minute in range(0,60):#range will go from start upto the end (excluding the end)
        print(f"hour is {hour} and minute is {minute}")

#For every university we wanted to define course
#Usecase: Create a program to iterate on all universities and offer all courses..
univ=['Anna','Bhari','Satyabama']
courses=['IT','MECH','CIVIL','EEE']

#Usecase1: Try create tables for our kids from 2 to how many tables (get as an input)?
#I need to create tables program for a given range of values until the given max table value
# Using simple or nested for loop, skip the 5 and 10 tables
#Try to enrich the above program with dynamically getting the input from the user to control
#starting table, total number of tables
#Below program is an example to cover 2 table alone
for i in range(1,11):
    print(f" 2 * {i} = {i * 2}")

max_table=int(input("enter the max table"))
max_table_values_iteration=int(input("enter the max table value iterate"))
start_table=1
#add the below feature to skip the 5 and 10 tables (after we learn continue statement)

'''
#use the below code for reference....
max_table=int(input("enter the max table"))
max_table_values_iteration=int(input("enter the max table value iterate"))
start_table=1
#1,2,3,4,6,7,8,9,11,12,13,14
#we need to use the nested for loop
for table in range(start_table,max_table+1):
    print("current iteration of the loop is ",table)
    #break will stop the complete iteration scope.
    #continue will stop executing the remaining code and go to next iteration
    #pass will pass the given line of code and proceed with remaining code
    if table in (5,10):
        print("skipping")
        continue #dont run the below loop, skip this iteration loop
    if table ==15:
        print("we reached maximum table count, hence breaking this loop and coming out of it")
        break
        #exit(0)#non error exit
    for value in range(1,max_table_values_iteration+1):
        print(f" {table} * {value} = {table * value}")
print("We are out of the loop....")
print("break will allow our program to futher run, 100 more lines of code to run")
print("exit will not allow our program to futher run, 100 more lines of code to run")
#exit(0)
'''

#For Loop with Break and Continue constructs/clauses:
#Break is used to break the execution of the loop by come out of the loop if a given condition matches
#Continue is used to skip the given iteration of the loop (and execute the next iteration) if a given condition matches
'''
continue - only used in looping, will stop executing the remaining code inside the loop and go to next iteration
break - only used in looping, will stop executing the remaining code and come out of the loop and executes the LOC after the loop
pass - will only pass that given line, but further lines inside the loop or after the loop will also run (nothing is affected)
exit - can be used anywhere to terminate the program with a non error (0) or error code >0
'''

#Usecase1: Write a program to apply tax 10% for all the states, other than pondy and goa (we use continue only for go and po)
states=['tn','an','ke','go','ka','po','mp']
print(f"state tax of 10% applicable for tn")
print(f"state tax is not applicable for go")
print(f"state tax is not applicable for po")

#Usecase2: Break statement usage : Eg. give only bonus to employees who is getting salary <15000
sal_lst=[10000,11000,13000,15000,20000,30000,40000]

#Looping constructs available in Common Prog languages -
#Looping constructs available in Python language -
#Types of Looping - Entry Control & Exit Control loops

#conditional & unconditional
#nested looping (for for/ for while/while for)
#constructs - break & continue & pass
#conditional (entry controlled & exit controlled)

#Realtime Example of using While loop: Entry controlled & Exit controlled loop
#Login username/password used in our routine life

#Do while loop (least bother) workaround in python to demonstrate "exit control loop"
#i am checking the condition in the exit, if  it doesn't met, i am breaking the loop
#after running the loop atleast once
movie_ticket=False
while True:#conditional but not entry controlled
    print("allowing a person inside the theater")
    if movie_ticket:#exit controlled
        print("allow to proceed further to watch the movie")
    else:
        print("checking him in the exit door, and sending him out to not continue the loop of watching movie")
        break

##############################################Condition Structure & Looping Constructs completed####################################

##############################################Condition Structure & Looping Constructs completed####################################


print('K. Collection (complex) Types')
#Application of using collection types in realtime world?
#Self served metadata driven Data movement automation (DMA) tool
#Banking credit card unstruct to semi struct to structure conversion using AI
#unstructured resumes -> AI engine semistruct (json) -> structured (database) -> ai (vectors) RAG -> companies (nlp)

#usecase: (we will implement soon)
#1. try to print from bigquery to gcs we are loading data
#2. try changing the query
#3. try using where clause also
#sqlquery="select custid,upper(custname) as upper_custname from customer where (city='chennai');"


#What is a complex/collection type? Semi structured data
#Collection is a datatype which is going to help us collect different data items/values/attribs/element in a collected/grouped fashion
#It leads to the next dimensions of data 2+(1/2/3...)
#it is flexible, dynamic, performant, complex, occupies less space in the storage and network transfer of data

#different collection types in the order of importance?
#list, dictionary, tuple, set
#Primary understanding + Examples of Collection Types:
#list []: - indexed sequenced collection of homogeneous elements
#salary of employees
#index    0      1     2
salaries=[10000,20000,40000] #indexed sequenced collection of homogeneous elements
print(type(salaries))

#dictionary {k1:v1,k2:v2}
#id and respective salary of employees {} - collection of key,value pair
#name wise salary
name_salaries={'irfan':10000,'rajesh':20000,'vini':40000}#looks like a json
id_salaries={1:10000,2:20000,3:40000}#looks like a json
print(type(id_salaries))

#tuple ():
#Address of Employees - indexed sequenced collection of hetrogeneous elements
address=(139,'5th main road','velachery','chennai',600042)

#set {values} :
#I wanted to store employee ids - set is a collection of unique items
customerid_WE47={1,2,3,4,7,6,10,13,11,150,120,1001,1000,10000,500,5000,1001}
customerid_W36={1000,10000,11000}
print(customerid_WE47.intersection(customerid_W36))

#Example of all collection types used:
#{'process': 'ETL Process1', 'source': {'hive', 'Bigquery'}, 'target': ['HDFS', 'GCS'], 'cols': ['custid', 'upper(custname) as upper_custname'], 'tablename': 'customer', 'where': "(city='chennai')", 'uris': ('gcs://abc/xyz_bucket/', 100)}

#Different types of collection types? in the order of importance
#list, dict, tuple, set

#Why we need collection types?
#To manage/store/parse the complex dataset in a hirarchical/nested/complex structure stored or to process semi structure data, nested data,
# dynamic schema-ful data (avro), variable data/metadata, for a data or metadata/configuration driven approaches..

#Different characteristics of collection types? we are going to learn in detail below..
#Iterable (looping), mutable (changable) - updatable (modifyable) & resizable (added/removed), accessible (select using index, position, value, key)

######What are the topics we have to learn in collection types#######
#Iterable? Yes, all collection types are iterable.
lst=[1,2,3]
dict1={1:10,2:20,3:30}
tup1=(1,2,3,'a','b')
set1={10,20,30}
for i in lst:
    print(i)
for i in dict1:
    print(i)
for i in tup1:
    print(i)
for i in set1:
    print(i)

#Notation, iterable, access, resizable/mutable/immutable?  insert/update/delete, functions to apply
#All the above we are going to see in detail
#Notation:[], {k,v}, (), {v1,v2}
#Accessed using ? index/key
# list [] - index - eg. list of salaries of employees
sal_lst=[10000,20000,25000,30000]
print(sal_lst[0])#using index starting from zero from left to right
print(sal_lst[-1])#using index starting from zero from right to left

sal_lst=[10000,20000,25000,30000]
#print("last sal of the list",sal_lst(len(sal_lst)-1))
#print("last sal of the list",sal_lst(len(sal_lst)-2))

# dict {k:v,k:v} - using key - eg. empid and name as a collection of k,v pair {1:'irfan',2:'deepika'}
dict1={1:'irfan',2:'deepika'}
dict2={'inceptez':"inceptez is a company",'google':"google is search engine"}
print(dict1[2])

# tuple () - index - eg. store a record/row of a table (cid,cname,age,city,pincode)
tup1=(1,'irfan',43,'chennai',600042)
print(tup1[1])

# set {}- items cannot be accessed individually because it is a set - eg.
#using iterator we can access all elements of the set
set1_iz_customers={1,2,3,4}
set2_iz_competitors_customers={4,5,6}
set1_iz_customers.intersection(set2_iz_competitors_customers)

#How oracle perform this query operation in the background?
'''
cid	name	city
1	irfan	chn
2	prem	hyd
1	vaanmathy	mum
'''
table_records=[ (1,'irfan','chn'),(2,'prem','hyd'),(1,'vaanmathy','mum') ]
cid_data=[]
for cid in table_records:
    cid_data.append(cid[0])
print(cid_data)#all cids
print(set(cid_data))

print("Deepdive into - list operations")
#Definition: Indexed, sequenced collection of HOMOGENEOUS elements
lst_sal=[10000,30000,20000]
#List can be hetrogeneous too (but not suggested, why ? because while operate between the elements of the list, program fails because python is a strongly typed language)
lst_sal=[10000,30000,20000,'Chennai']
#sum(lst_sal) fails, hence hold similar/homogeneous data in list preferrably

#select/access - using index starts from 0
lst_sal=[10000,30000,20000]
print(lst_sal[0])
for i in lst_sal:
    print(i+1000)

#insert/update/delete (list is mutable, hence updating and resizing (add/removing) is possible)
#append in the last (proves list is mutable/resizable/can be inserted)
lst_sal=[10000,30000,20000]
lst_sal.append(30000)#list is resizable & we can insert elements into the list

#insert in the index position (resizable)
lst_desig=['SE','TL','PM']
lst_desig.insert(1,'SSE')#How to understand a function by hovering & how to not memorize the function

#update the list elements (mutable)
lst_desig=['SE','TL','PM']
lst_desig[1]='SSE' #updated

#delete the elements of the list using value
lst_desig=['SE','TL','PM']
lst_desig.pop()#delete index value of -1 (PM)

#pop (delete) the elements of the list using index
deleted_item_returned=lst_desig.pop(1)#delete index value of 1 (TL)
print(deleted_item_returned)

#delete a particular element directly
lst_desig=['SE','TL','PM','TL']
if lst_desig.count('TL')>=1:
    lst_desig.remove('TL')

#if I need to remove all occurance at a time ? is there any removeAll method
lst_desig=['SE','TL','PM','TL','PM','TL','TL']
for i in range(0,lst_desig.count('TL')):
    lst_desig.remove('TL')

#Delete entire elements of the list regardless of index
lst_desig=['SE','TL','PM']
lst_desig.clear()

#search for a value with in the given index (range) value and pop(remove) it
lst_desig=['SE','TL','PM','DH','TL']#particular element in a given index can be deleted
lst_desig.pop(lst_desig.index('TL',2))#start from index of 2

#Wanted to remove the duplicate in a given list?
lst_desig=['SE','TL','PM','DH','TL']
print(list(set(lst_desig)))#by casting to set and back to list we can achieve it...

print("Dictionaries (mutable) - {k:v, k:v}")#collection of key,value pair, where key is unique and value can be anything...
lst_sal=[10000,20000,30000,50000,40000]
for i in lst_sal:
    print("sal+bon commonly",i+1000)

dict_cid_sal={1:10000,2:20000,3:30000,4:50000,5:40000,2:45000}
dict_cid_name={1:'irfan',2:'b',3:'c',4:'d',5:'e'}

#Access a dictionary - using key
print("salary of custid 3 is ",dict_cid_sal[3])

#Whether dictionary is resizable? yes
#Adding Items - if the key is not found
dict_cid_sal.update({6:50000})#insert (since key is not present)

#Whether dictionary is updatable/mutable?
#Updating Items - if the key is found
dict_cid_sal.update({1:20000})#update (since key is already present)

#Removing an Item (from the last) resizable
dict_cid_sal.popitem()

#Delete(pop) the given key resizable
dict_cid_sal.pop(4)

#Delete all the elements of a dict resizable

#Iteration of Dictionary
#Iterate on the items of the Dict - will return what data and what datatype???
print(dict_cid_sal.items())#returns list(tuple) type

#Iterate on the keys of the Dict - will return what datatype???
print(dict_cid_sal.keys())#returns list type

#Iterate on the values of the Dict - will return what datatype???respective value's datatype
print(dict_cid_sal.values())#returns list type

#fromkeys function to create a dictionary from any iterable types with the default values added
dict_cid_sal={}
lst_emp=[1,2,3,4]
dict_cid_sal=dict_cid_sal.fromkeys(lst_emp,10000)

#Setdefault (only do insert) will add the key and value provided if key is not present already, if already present consider the given value and not the default value
dict_cid_sal={1:10000,2:20000}
dict_cid_sal.setdefault(3,30000)#do addition of default key and value to the given dictionary
dict_cid_sal.setdefault(2,30000)#do not add/update anything

print("Tuples (immutable?)")
#Definition of Tuple:Tuple is an indexed sequenced collection of hetrogeneous elements, tuples are immutable (non updatable and non resizable)
#Notation is - ()
tup_address=(139,'5th main road','velachery',600042,'velachery')
tup_row=(1,'irfan',43,'chennai')

#select/access - using index
print(tup_row[1])

#count of some element in the given tuple
print(tup_row.index('irfan',0,4))
#search for some element in the given tuple to identify the index
print(tup_address.count('velachery'))
#tuple is similar to list using the below functions...
#print([1,2,3,2].count(2))
#print([1,2,3,2].index(2,0,2))

#Resizable? No (insert/delete)
#Try to Add some elements to the tuple
#Insert/Append?
#tup_row.__add__(9840800131)#doesnt work

#delete? No pop/delete/clear...
#tup_row.__del__()#doesnt work

#Modify (update) - Not possible (immutable)
#tup_row[2]=44 #This will not work...

#I want to achieve Insert/update/Delete in a tuple? Not possible by default,
# but we can do some workaround to achieve it?
tup_address=(139,'5th main road','velachery',600042,'velachery')
lst_tup_address=list(tup_address)
lst_tup_address.pop(-1)
tup_address=tuple(lst_tup_address)

#Least important in terms of python, but for analytics set operations are important
#especially (union, union all, intersection, difference, symmetric difference, adjoint/disjoint, subset/superset)
print("Set (mutable) (least important)- Notation {} - "
      "Set is a distinct collection of iterable elements, cannot be accessed using index/keys ?? Why? because it is a set "
      "and sorted (upto 255 numbers)")
custid_lst=[1,2,3,4,5,6]
#When do we go for set, comparing with list?
custid_set={1,2,3,4,5,6}#better to have in set, because by default it is unique
#If we want to do set operations, then set is a right option
asid_noninceptez={3,4,5,6}
asid_inceptez={1,2,3,4}
print("who are all the aspirants learned from other institute, learning here in Iz also?",
      asid_noninceptez.intersection(asid_inceptez))
print("who are all the aspirants learned only from Iz?",
      asid_inceptez.difference(asid_noninceptez))

#how to access the element of a set (cant be access directly by using index/key/values)- Index can't be used why?
#The number of elements/items in the set is not fixed in the numbers or sort order
custid_set={1,2,3,4,5,6}
#custid_set[0] #not possible to access using index
list(custid_set)[0] #possible to access using index, if converted to list

#set is internally sorted upto (255 values) because it uses some hasing algorithm
custid_set={1,2,5,6,7,3,4}
#how to sort?
list(custid_set).sort(key=None,reverse=True)
custid_set={1,2,3,4,5,6}

#set is iterable?yes
for i in custid_set:
    print(i)

#set is mutable (resizable) - Add/Removing/popping/cleaning - yes
#add will help add/update an element on the set
custid_set={1,2,3,4,5,6}
custid_set.add(7)

custid_set.remove(3)#remove out the given element
custid_set.pop()#popping out the elements #delete in database
custid_set.clear()#truncate in database

#set is mutable? yes
#update will help add/update another set (merge/upsert/insert else update)
custid_set2={7,8,9,10,11}
custid_set.update(custid_set2)

#Our aim is not learning how to do set operations in python...
# but this learning will help us understand the concept of set operation in SQL..
#set is supported with set operation (If we use set, we use it for these purposes)
#Requirement of identifying the common department in the given set

#Lets do some set operations...
#Fundamental set operation (must know commonly, but not interms of python)
asid_inceptez={1,2,3,4}
asid_noninceptez={3,4,5,6}

#To perform unionall (it support duplicate also)
lst_all_aspirants=list(asid_inceptez)
lst_all_aspirants.extend(asid_noninceptez)#equivalent to union all
print(lst_all_aspirants)

print("who are all the overall aspirants, regardless whether they are learning only from IZ or from other places also",
      asid_inceptez.union(asid_noninceptez))#{1,2,3,4,5,6}
print("who are all the aspirants learned from other institute, learning here in Iz also?",
      asid_noninceptez.intersection(asid_inceptez))#{3,4}
print("who are all the aspirants learned only from Iz?",
      asid_inceptez.difference(asid_noninceptez))#{1,2}

#Few misceleneous set operations are available- deeper analytical functionalities
asid_inceptez={1,2,3,4}
asid_wd36={1,2}
asid_we47={3,4}
asid_someotherbatch={10,11,1}
#superset (help you find whether the given subset is belonging to a larger set)
print("does inceptez is a super set (owning this batch) of the wd36 batch or wd36 batch is a subset of inceptez",
      asid_inceptez.issuperset(asid_wd36))
print("does inceptez is a super set (owning this batch) of the wd36 batch",
      asid_inceptez.issuperset(asid_someotherbatch))

#Before joining set of data, check whether they are joinable with some common values? disjoint
asid_inceptez={1,2,3,4}
asid_noninceptez={3,4,5,6}
asid_noninceptez.isdisjoint(asid_inceptez)#False
#adjoint means, do we have non commanality
print(not(asid_noninceptez.isdisjoint(asid_inceptez)))#True

asid_inceptez={1,2,3,4}
asid_noninceptez={5,6}
asid_noninceptez.isdisjoint(asid_inceptez)#True
print("is there any commanality between 2 sets, does inceptez is disjointed (no one from inceptez learned from other centers",asid_inceptez.isdisjoint(asid_noninceptez))

#symmetric difference
asid_inceptez={1,2,3,4}
asid_noninceptez={3,4,5,6}
print("who are all non common between inceptez and non inceptez",
      asid_inceptez.symmetric_difference(asid_noninceptez))#{1,2,5,6}
#to understand how symmetric_difference works, used this formula #a-b union b-a
print((asid_inceptez.difference(asid_noninceptez)).union(asid_noninceptez.difference(asid_inceptez)))#{1,2,5,6}

#We can do update of this result also into the first set
asid_inceptez.symmetric_difference_update(asid_noninceptez)
print("updated set",asid_inceptez)

#Final usecase relating collection types (list/dict): strategic/smart
#DMA/DMT tool
#read from filesystem -> transformation -> load target
#parsing (decode/understand) of json config file using python collection types and convert that into sql and program to ETL

#dma.json
#{"process":"ETL Process1","source":["hive","Bigquery"],"target":["HDFS","GCS"],"cols":["custid","upper(city) as upper_city"],"tablename":"customer","where":"(city='chennai')","gcs_uri":"gcs://abc/xyz_bucket/"}
datasample={'process': 'ETL Process1', 'source': ['hive', 'Bigquery'], 'target': ['HDFS', 'GCS'], 'cols': ['custid', 'upper(city) as upper_city'], 'tablename': 'customer', 'where': "(city='chennai')", 'gcs_uri': 'gcs://abc/xyz_bucket/'}
fileopened=open("C:\\dataset1\\dma.json")
import json
identify_json_data=json.load(fileopened)
print(type(identify_json_data))
print(identify_json_data)

#Form a sql query from the given config file to select data from the given columns from the given table customer with the where clause applied?
sql_query="select custid,upper(city) as upper_city from customer where (city='chennai')"

dict_lst={1:['mohamed','irfan'],2:['divya','dharshini']}
print(dict_lst[1][1])


#finally today, we will enrich this program with log of additional file handling techniques
# and exception handler blocks used
try:
    import json
    filename=input("enter the filename")
    location="C:\\dataset1\\"
    loc_file=location+filename
    file_open_from_disk_mem=open(loc_file)
    print("file opened successfully")
    #file_open_from_disk_mem=open("C:\\dataset2\\dma.json")
    json_file=json.load(file_open_from_disk_mem)
    print("parsing the file")
    all_lst_cols=json_file["cols"]
    col1=all_lst_cols[0]
    col2=all_lst_cols[1]
    tabname=json_file['tablename']
    sqlquery=f"select {col1},{col1} from {tabname}"
    list_source_user_chosen=json_file['source']
    second_source=list_source_user_chosen[1]
    print(f"run this query in the source database of {second_source} ",sqlquery)
except Exception:#handler block
    print("Pls ensure path is correct")
    print("Pls ensure filename is correct or file has read access")