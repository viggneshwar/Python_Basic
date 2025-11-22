'''
What is a Function/Method? Aspirant's response?
#block of code stored in a name, designed to perform a specific/set of tasks...
#can be reused by anyone, any number of times, from anywhere,
# concurrently, parallely, distributedly, asynchronously

Ways of Creating Functions? Minimum we all have to know
#mandatorily these 5 concepts
1. Minimum way of creating a function
2. Optimal way of creating a function
3. Different possible 4 ways of creating functions (fun with no inp/out, only inp, only out, inp/out) eg. DB & FS ops
4. Call a function and get the result and store in a variable/print the result
5. Possible ways of invoking the functions passing/using the different argument types (5 types)
6. Advanced topics (special types of functions) (dont worry, its for interview)
'''

#FUNCTION BASED PROGRAMMING (Python is a pure FBP Language, Python treats Functions as first class citizen)
#What? Function/Method is a stored program that perform specific/set of tasks

#Why we need to create Functions or why we need FBP -
#1. Functions can be created once and reused multiple times - reduced complexity, reduced LOC, Precise/simple/ease of understanding, Maintainable
#2. Functions help us reduce the LOC by reusing and by composing
#3. Functions are used for creating Application or Organization specific Reusable Frameworks

#All about Functions or Methods in FBP - syntactically...
###################################################
#1. How to Create a function and call a function (High level)
#1. Minimal/least way of creating a method
#define a function/method with basic/minimum syntax
def fun_name():
    print('hello world')

#how to call a function to get it executed
fun_name()

#2. Regular/Standard/Optimal/typical/formal way of creating a method
def calc_custom_sqrt(input_num_arg:int):#irfan pinged
    '''this function take input from user and return the sqrt of the given input'''
    sqrt_calc=input_num_arg*input_num_arg#jeeva processed it
    return sqrt_calc#pinged back

#How to call a function with necessary arguments passed and store the return result in another variable
result_returned=calc_custom_sqrt(10)

#How to use/print that variable subsequently
print(result_returned)

#We need to have a def keyword (definition of a function) - (mandatory) any function/method creation has to have starting with def keyword
#followed by the function name - (mandatory), lower case with underscores or just lowercase words (snakecase/lowercase)
# mentioned inside the brackets() - mandatory
#followed by argument(s) - optional
# with datatype mentioned (to hint us understand the datatype signature of the method)- optional
#followed by ':' (completion of the definition) - mandatory
#followed by - some description in ''' , to display the methods description when hover - optional
#followed by the body of the program (one/multiple lines of code - core logics + std output + return) - mandatory with atleast 1 line
#followed by return keyword - (optional) where as return help us send back result to the calling environment

#3. What are the possible way of creating functions/methods
#all 4 permutation and combination works...
# (fun with no inp/out, only inp, only out, inp/out)
# eg. Analogical examples of DB & FS operations
#use learning_db;#function with no input and no output
#a.Method with no input arguments and no return - eg. select without any return, just print
import shutil
def use_learning_db():
    print("this function when called, will execute this statement and poing to the learning_db--> use learning_db;")
use_learning_db()
#Reallife example relating SQL database query? #function with no input and no output
#use learning_db;

#Usecase1: I wanted to clean the tmp folder in a predefined path C:\\dataset1\\tmp, if it exists
def clean_tmp():
    import os
    if os.path.exists("D:\\dataset1\\tmp"):
        shutil.rmtree("D:\\dataset1\\tmp")
        print("tmp path delete successfully")
    else:
        print("no tmp path present")


print(clean_tmp())
#b.Method with input arguments and no return - eg. create a specific database/insert row into a table.
def insert_into_sampletbl(col1:int):
    print(f"this function when called, will execute this statement and insert value to the column--> insert into sampletbl values({col1});")

print(insert_into_sampletbl(11))

#Reallife example relating SQL database query? #fun with input but no output
#insert into sampletbl values(10);

#Usecase2: I wanted to clean the tmp folder in a any input path C:\\dataset1\\tmp passed as an argument, if it exists

#c.Method with no input arguments but return - #fun with no input but output is there
def select_cur_dt():
    import datetime
    return datetime.datetime.now()

curdt=select_cur_dt()
print(curdt)
#Reallife example relating SQL database query?
#this function will collect the server date/time and return to the python environment
#select current_date();

#Usecase3: I wanted to clean the tmp folder in a given input path C:\\dataset1\\tmp,
# if it exists and return the status of True/False


#d.Method with input arguments and return -


#Reallife example relating SQL database query? count the number of tables in a db passing dbname as input and getting count as output
#select count(*) from sampletbl where id in (10);#fun with input and produce output

#Usecase4: I wanted to clean any input folder in a given input path C:\\dataset1\\anything, if it exists and return the status
def clean_anypath(inputpath:str):
    import os
    if os.path.exists(inputpath):
        shutil.rmtree(inputpath)
        print(f"{inputpath} path delete successfully")
        return True
    else:
        print(f"no {inputpath} path present")
        return False
return_status=clean_anypath("D:\\dataset1\\accounts.csv")
print(return_status)

#4. How do we call the Methods/function: what is the difference between print and return
#How to handle the return result of the above function ? by assigning it in a variable or print it
def fun1(number):
    res=number*number
    print("inside fun1",res)
print(fun1(10))#fun1 print will produce output in the screen and return is none

def fun2(number):
    res=number*number
    print("inside fun2",res)
    return res
print(fun2(10))#fun2 print will produce output in the screen and return the value also to again printed/used outside

#Simple usecase (Strategic):
# a. Complete the Swiggy/zomato usecase (anonymous program) by creating a formal reusable method/function
# b. and add exception handling also in it..

#5. How to create & call the methods using different Argument types: Important part
##############################################################################
#Different methdologies of passing arguments to the functions while calling the function:
#I want to give salary to employees by deducting pf
def sal_calc(sal:int,pf:int):
    final_sal=sal-pf
    return final_sal

#A. Positional arguments methods - Calling the function with the arguments passed positional
calculated_sal=sal_calc(100000,5000)#positional arg function
print(f"let me deposit {calculated_sal} in the bank")

#B. Named/keyword arguments methods
#named arg fun
calculated_sal=sal_calc(pf=5000,sal=100000)#named/keyword arg function
print(f"let me deposit {calculated_sal} in the bank")
calculated_sal=sal_calc(5000,100000)#positional will not work, result in wrong values
print(f"let me deposit {calculated_sal} in the bank")

#Mixing positional & named? yes, but with a restriction
def sal_calc(sal:int,pf:int,incentive:int):
    final_sal=(sal-pf)+incentive
    return final_sal
calculated_sal=sal_calc(100000,incentive=1000,pf=5000)#possible (can use keyword/named after positional
#calculated_sal=sal_calc(sal=100000,5000,1000)#not possible (we cant use positional after named/keyword)

#c. Default arguments methods - If the function is not called with enough argument values, then default value can be used
def sal_calc(sal:int,pf:int,incentive=1000):
    final_sal=(sal-pf)+incentive
    return final_sal

calculated_sal=sal_calc(100000,5000,2000)
print(f"let me deposit {calculated_sal} in the bank")
calculated_sal=sal_calc(100000,5000)
print(f"let me deposit {calculated_sal} in the bank")

#Usecase4 (reiterate):
# I wanted to clean any input folder in a given input path C:\\dataset1\\anything,
# if it exists and return the status,
# if the user is not passing the input path, then it has to be defaulted with tmp folder

#Write the function here with default argument methodology??

#return_status=clean_anypath("D:\\dataset1\\accounts.csv")#positional arg function
#print(return_status)
#return_status=clean_anypath(inputpath="D:\\dataset1\\accounts.csv")#named arg function
#print(return_status)
#return_status=clean_anypath()#default arg function
#print(return_status)

#d. Arbitrary (any numbers) Argument Method/Function -
# Accepts the argument as tuple with the notation of *argument_name
# If we are not sure about the number of arguments that we are going to pass to this method,
# but we use the same order (position) of passing the arguments

#Usecase: I want to create a mail id for the users, users will give fname,lname & domain or only they give fname and lname
#requirement:
# if i call the above function with 3 arguments like fname,lname,domain then it should return fname.lname@domain.com
# if i call the above function with 2 arguments like fname,lname then it should return fname.lname@inceptez.com
# if i call the above function with 1 argument like fname then it should return fname.na@inceptez.com
#if no param is passed just print, minimum name is needed...
def generate_mail(*args):
    print("type of arb argument is Tuple",type(args))
    if len(args)==3:
        fname = args[0]
        lname = args[1]
        domain = args[2]
        final_mail = fname + '.' + lname + '@' + domain
    elif len(args)==2:
        fname = args[0]
        lname = args[1]
        final_mail = fname + '.' + lname + '@inceptez.com'
    elif len(args)==1:
        fname = args[0]
        final_mail = fname + '.na@inceptez.com'
    else:
        print("give atleast one argument")
    return final_mail

#Benifit of arbitrary arg function - we can pass any number of params dynamically
#Challenge is - we have to manipulate/compute the logic with the right positions used
print(generate_mail('jeevitha'))
print(generate_mail('loganathan','sundaram'))
print(generate_mail('loganathan','sundaram','cts.com'))


#Purely talks about arbitrary (positional) arg function realtime example
#Usecase: strategic - arbitrary arg function works only if the expected number of arguments are passed, otherwise we have to handle it programatically


#Usecase strategic (arb arg, default arg, arb keyword arg): Create a method to calculate sal+bonus+incentives for differenct IT companies using either arbitrary keyword arg function
#Hewitt/HRworkways..
#CTS, Infy, HCL calculate sal+bon+inc
# where CTS give all the 3 components
# Infy gives only first 2 components
# HCL gives only first 1 component
#We need to get the results as given below..
#calc_gross_sal(comp='CTS',sal=100000,bon=10,inc=5000) -> 115000
#calc_gross_sal(comp='INFY',sal=100000,bon=5) -> 105000
#calc_gross_sal(comp='HCL',sal=100000) -> 100000
#arb arg, default arg


#e. Keyword Arbitrary Argument Method/Function - Accepts the argument as  with the notation of **argument_name
# If we are not sure about the number of arguments that we are going to pass to this method and
#the order of the argument we are going to pass is unknown (Named arguments) , we can use keyword arbitrary arg method
#Benifit of arbitrary keyword arg function - we can pass any number of params dynamically (using named notation)
#Challenge is - No challenges, any way it works... just use dict.get('key','default value')
dict1={'fname':'mohamed','lname':'irfan'}
print(dict1.get('fname'))

def generate_mail(**kwargs):
    print("type of arb argument is Dictionary",type(kwargs))
    print("value in the kwargs",kwargs)
    fname=kwargs['fname']
    lname = kwargs.get('lname','na')
    domain = kwargs.get('domain','inceptez.com')
    final_mail = fname + '.' + lname + '@' + domain
    return final_mail

generate_mail(fname='mohamed',lname='irfan',domain='cts.com')
generate_mail(lname='irfan',fname='mohamed',name='girish')
generate_mail(fname='mohamed',lname='irfan')
generate_mail(fname='mohamed')


#Usecase strategic: Create a method to calculate sal+bonus+incentives for differenct IT companies
# using arbitrary arg function
#calc_gross_sal('CTS',100000,10,5000) -> 115000
#calc_gross_sal('INFY',100000,5) -> 105000
#calc_gross_sal('HCL',100000) -> 100000

# using arbitrary keyword arg function
#Hewitt/HRworkways..
#CTS, Infy, HCL calculate sal+bon+inc
# where CTS give all the 3 components
# Infy gives only first 2 components
# HCL gives only first 1 component
#We need to get the results as given below..
#calc_gross_sal(comp='CTS',sal=100000,bon=10,inc=5000) -> 115000
#calc_gross_sal(comp='INFY',sal=100000,bon=5) -> 105000
#calc_gross_sal(comp='HCL',sal=100000) -> 100000

#Till above lines it is important... below part is not important


#6. Special Types of Methods/Functions in Python - HOF, Closure, Lambda, Recursive...
# Is not much important for creating/implementing the methods by Dataengineers,
#but for understanding the type of methods/functions used in the framework, the below learning is useful.
# FBP (special methods) - Higher Order Function, Anonymous/lambda/function literal/value function,Closures, recursive functions/tail recursion

print("**********Special Types of Methods/Functions in Python - Important (interview purpose)***************")
#a. Higher Order Functions/Currying function/partial function
#Higher order function (type1) is function which takes another function as an input
# (traditionally a function says - i take an input of some values but hof1 says i take an input of some program/function also)
#Higher order function (type2) is function that returns another function as a return type
# (i produce result of some values but hof2 says i produce some program/function also as a result/return))
print("Benifits of HOF1 -> 1. We can use the functions seperately or along with other functions "
      "2. Rather than rewriting the code in a given function we can reuse it by passing the function as an argument ")


print("b. Closures Functions")
print("What is closure? If the result of a given method is changed/affected by the value defined outside of the given function ")
#closure function
#Closure (function have a close connectivity with the external values)
# - If a value defined outside of a given function is impacting the result of a function

#Usecase Can you create a method called calc_sal_bonus_incentive using closure concepts?

print("c. Lambda Function - A function created anonymously or a function as a variable using lambda keyword")
#Lambda functions can be called as function literal/anonymous function/value function


print("d. Recursive Function or tail recursion - A function called by itself repeatedly or recursively")

#Realtime example of Recursive Function? SIP, FD, Complex Interest (interest for interest)
#I am investing 100000 rupees with an return of 10% year over year, after 3 years what is my return?
#100000 -> 100000+10000=110000 (year1) -> 110000+11000=121000 (year2) -> 121000+12100=133100 (year3)

#Lets write the above function in a single recursive function


#7. Scope of Variables in Functions/Methods - Local and Global variable
print("7. Scope of Variables in Functions/Methods - Local and Global variable")
print("a. Local Variable - variable created inside a function is local by default")

print("b. Global Variable - No need of global keyword, since by default variable in module is global")

print("c. Local Variable defined as global inside the function - By using global keyword we can achive")
