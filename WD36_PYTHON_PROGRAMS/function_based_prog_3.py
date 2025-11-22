'''
What is a Function/Method? Aspirant's response?
# collection of stored statements used to perform some specific task
#Function is a reusable code (used to handle repetitive tasks)
#is a stored program
#composable - we can marry multiple functions to achieve a complex functionality
#is a sub-routine
#perform some tasks (based on the input passed) and return the result - any permutaion & combination we can create a function
#first class citizen in python (FBP) - functions are also treated as like variable & values
#simple/elegant - use, maintain, understand & reason out
#will not change based on time

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
def name_of_function():
    pass
#define a function/method with basic/minimum syntax
def greeting():
    print("hello team")

#how to call a function to get it executed
greeting()
greeting()

#2. Regular/Standard/Optimal/typical/formal way of creating a method
def regular_function(param1:int, param2):
    '''This function is going to add arguments
    and return the result of the addition.....'''
    result=param1+param2
    return result

def bonus_calc(sal:int,bon:int):
    '''This function is going to do calculate the sal
    and bonus passed as an argument by the user
    and returns the bonus applied salary to the clling environment.....'''
    total_sal=sal+bon
    #return None
    return total_sal
#How to call a function with necessary arguments passed and store the return result in another variable
irfan_sal_bon=bonus_calc(10000,1000)
#How to use/print that variable subsequently
print("irfan salary before tax is ",irfan_sal_bon)
irfan_sal_bon_tax=irfan_sal_bon-(irfan_sal_bon*.10)
print("irfan salary after tax is ",irfan_sal_bon_tax)
print("shan salary is ",bonus_calc(20000,2000))

def name_of_function():
    pass
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
#a.Method with no input arguments and no return - eg. select without any return, just print
def fun1():
    print("hello")#static tasks it will execute
fun1()

#Reallife example relating SQL database query? select current_date();
def select_curdt():
    print("'select current_date();', going to print the cur date -> ",'2025-11-11')
select_curdt()

#Usecase1: I wanted to clean the tmp folder in a specific path C:\\dataset1\\tmp, if it exists
def clear_tmp():
    '''clean the tmp folder in a predefined specific path C:\\dataset1\\tmp, if it exists, print delete/not exist'''
    pass

#b.Method with input arguments and no return - eg. create a specific database/insert row into a table.
def fun1(a):
    print(a*a)
fun1(2)

#Reallife example relating SQL database query? create database input_db;
def create_db(dbname:str):
    print(f"create database {dbname}")
def insert_tbl_data(tabname:str,colvalues:str):
    print(f"insert into {tabname} values ({colvalues})")
print(insert_tbl_data('customer','custid'))

#Usecase2: I wanted to clean the tmp folder in a any input path C:\\dataset1\\tmp, if it exists
def clear_any_path(path):
    '''clean the tmp folder in a any input path {path}, if it exists, print delete/not exist'''
    pass

#c.Method with no input arguments but return - eg.
def fun1():
    result=2*2
    print(result)
    return result
fun1()

#Reallife example relating SQL database query? select current_date(); use this output for some other purposes further
#this function will collect the server date/time and return to the python environment
def select_return_curdt():
    res='select current_date();'
    print("'select current_date();', going to print the cur date -> ",res)
    return res

cur_dt=select_return_curdt()
import datetime
print("Local system date is ",datetime.date.today())
print("US server date is ",cur_dt)

#Usecase3: I wanted to clean the tmp folder in a given input path C:\\dataset1\\tmp, if it exists and return the status
def clear_tmp():
    '''clean the tmp folder in a predefined specific path C:\\dataset1\\tmp, if it exists, return true/false status'''
    pass

return_status=clear_tmp()
if return_status==True:
    print("tmp directory delete successfully, proceed further")
else:
    print("tmp directory is not exists/not  delete, stopping my further execution of program")
    exit(0)

#d.Method with input arguments and return - eg.
def fun1(a):
    result=a*a
    print(result)
    return result
ravali_notebook=fun1(3)

#Reallife example relating SQL database query? count the number of tables in a db passing dbname as input and getting count as output
def select_no_of_table_in_db(dbname:str):
    count_of_tbls=f"select count(*) from information_schema.tables where schema_name='{dbname}'"
    print(count_of_tbls)
    return count_of_tbls

table_cnt_python_variable=select_no_of_table_in_db('edwdb_kasi')
if table_cnt_python_variable>=3:
    print("kasi did some huge learning of database")
else:
    print("kasi did some simple learning of database")

#Usecase4: I wanted to clean any input folder in a given input path C:\\dataset1\\anything, if it exists and return the status
def clear_anypath(inputpath):
    '''clean the input argument folder path C:\\dataset1\\anypath, if it exists, return true/false status'''
    pass

return_status=clear_anypath("C:\\dataset1\\anypath")
if return_status==True:
    print("C:\\dataset1\\anypath directory deleted successfully, proceed further")
else:
    print("C:\\dataset1\\anypath directory is not exists/not  delete, stopping my further execution of program")
    exit(0)

#4. How do we call the Methods/function: what is the difference between print and return
def simple_fun(arg1:int):
    res1=arg1+100
    res2 = arg1 + 200
    print(res1)#prints 1100 (scope is completed inside the function)
    return res2#returns 1200 (scope is outside the function)
#How to handle the return result of the above function ? by assigning it in a variable or print it
return_value=simple_fun(1000)#1200
print(return_value)#1200

#Simple usecase (Strategic):
# a. Complete the Swiggy/zomato usecase (anonymous program) by creating a formal reusable method/function
# b. and add exception handling also in it..

#5. How to create & call the methods using different Argument types: Important part
##############################################################################
#Different methdologies of passing arguments to the functions while calling the function:
#A. Positional arguments methods - Calling the function with the arguments passed positional
# eg. sub(10,20) assigns 1st arg with 10 and second with 20
def subtraction(a,b):
    return a-b
#pos arg fun
res=subtraction(10,20)
print(res)
res=subtraction(20,10)
print(res)

#B. Named/keyword arguments methods
#named arg fun
res=subtraction(b=10,a=20)
#Mixing positional & named? Yes, first go with position then with name, reverse will not work
#res=subtraction(a=20,10)#this will not work
res=subtraction(20,b=10)

#c. Default arguments methods - If the function is not called with enough argument values, then default value can be used
def subtraction(a=0,b=0):#default the input arg with some values
    return a-b
res1=subtraction(20,10)#it will not use default values, input arguments overrides the default values
res2=subtraction(20)#a as 20 and b as 0, used positional
res3=subtraction(b=10)#a as 0 and b as 10, can we use positional? no, only named can be used

#Usecase4 (reiterate):
# I wanted to clean any input folder in a given input path C:\\dataset1\\anything,
# if it exists and return the status,
# if the user is not passing the input path, then it has to be defaulted with tmp folder
def clean_input_path(path_to_clean:str="C:\\dataset1\\tmp"):#This is a default arg function
    import shutil
    import os
    if os.path.exists(path_to_clean):
        print(f"{path_to_clean} path exists, cleaning it")
        shutil.rmtree(path_to_clean)
        return True
    else:
        print(f"{path_to_clean} path is not exists")
        return False

print("clear the temp",clean_input_path())
print("clear the user input path",clean_input_path("C:\\dataset1\\somepath"))
print(f"""clear the user input path {clean_input_path("C:\\dataset1\\somepath")}""")

#3 Usecases:
# I want to create a function to calculate sal+bonus and call the function using pos, named and default args (if bonus is not defined default it as 1000)

#d. Arbitrary (any numbers) Argument Method/Function -
# Accepts the argument as tuple with the notation of *argument_name
# If we are not sure about the number of arguments that we are going to pass to this method,
# but we use the same order (position) of passing the arguments
def subtraction(*a):#arbitrary argument function
    print(a)
    print(type(a))
    return a[0]-a[1]#return a-b

#Usecase: I want to create a mail id for the users, users will give fname,lname & domain or only they give fname and lname
def generate_mail(fname,lname,domain):
    mailid=fname+'.'+lname+'@'+domain
    return mailid

#Purely talks about arbitrary (positional) arg function realtime example
#Usecase: strategic - arbitrary arg function works only if the expected number of arguments are passed, otherwise we have to handle it programatically
def generate_mail(*args):
    len_of_args=len(args)
    if len_of_args==1:
        mailid = args[0] + '.' + 'na' + '@' + 'inceptez.com'
    elif len_of_args==2:
        mailid = args[0] + '.' + args[1] + '@' + 'inceptez.com'
    elif len_of_args == 3:
        mailid = args[0] + '.' + args[1] + '@' + args[2]
    else:
        print("no input passed")
        return None
    return mailid
print(generate_mail('amarendar'))
print(generate_mail('mohamed','irfan'))
print(generate_mail('siva','thangavelu','cts.com'))

def generate_mail(*args,domain='inceptez.com'):#arbitrary(positional) arg + default argument + named argument
    len_of_args=len(args)
    if len_of_args==1:
        mailid = args[0] + '.' + 'na' + '@' + domain
    elif len_of_args==2:
        mailid = args[0] + '.' + args[1] + '@' + domain
    else:
        print("no input passed")
        return None
    return mailid
print(generate_mail('amarendar'))
print(generate_mail('mohamed','irfan'))
print(generate_mail('siva','thangavelu','cts.com'))#domain is also considered as arbitrary argument
print(generate_mail('siva','thangavelu',domain='cts.com'))#we have to explicitly define domain as named argument


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

def calc_gross_sal(*args):#we can go with arbitrarty positional arg func with the known logics to handle different arguments
    compname=args[0]
    if compname=='CTS':
        sal=args[1]
        bonpct = args[2]
        inc=args[3]
        bonus_applied_sal = sal + (sal * (bonpct / 100))
        bonus_inc_applied_sal=bonus_applied_sal+inc
        return bonus_inc_applied_sal
    elif compname=='INFY':
        sal = args[1]
        bonpct = args[2]
        bonus_applied_sal = sal + (sal * (bonpct / 100))
        return bonus_applied_sal
    elif compname=='HCL':
        sal = args[1]
        return sal
    else:
        return None







#e. Keyword Arbitrary Argument Method/Function - Accepts the argument as  with the notation of **argument_name
# If we are not sure about the number of arguments that we are going to pass to this method and
#the order of the argument we are going to pass is unknown (Named arguments) , we can use keyword arbitrary arg method


#Usecase strategic: Create a method to calculate sal+bonus+incentives for differenct IT companies
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
