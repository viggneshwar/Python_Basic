#EXCEPTION HANDLING
#Understanding of Exception: what? unexpected event occured while executing a program (non zero exit), if we have a handler/mitigation for an exception then it is exception handler
#exception handler blocks (try, except, else, finally)

#Types of Exception: Predefined ()
# & Userdefined/CustomExceptions ()

print("1. Fundamendals of Exception Handling")
print("What? When an unexpected event occured, how to handle that without making the program abruptly terminated")
print("Exception handling blocks: try, except, else & finally")
#Analogical/layman understanding
'''
try: 
    plan for doing some purchase
    getting ready
    ensure i have the purse in my hand
    start my bike/car
    entering shop
    adding some products in the cart
    purchasing it
    staring my car/bike and dropping it in the parking
    start my wfh work

except planaborte as message: (try is failed)
    put alternative plan/i have to abort plan (conveincing my wife/kids)
cantgetready as message:
    try with drinking water
pursenotfound as message:
    let me carry cash

else:#no exception occured (try is success)
    check for the product quality
    clean my vehicle
finally:#at any cost, whether my try is success or failed
    i will have my lunch
'''
#try: The main (mandatory) block where the main program is writtened
#except: The exception handler (optional) block where the handler program is writtened
#else: The else (optional) block of except block (if try is success then go to else, if except is success then don't go to else)
#finally: This is a default block (optional) that runs always at any cost (whether try/except/else is success/fail
import json
import shutil
import os
try:
    userinput = input("enter the file to read")
    tmpath="C:\\dataset1\\tmp"
    fullpath=f"C:\\dataset1\\{userinput}"
    #block1 (seperate activity1)
    if os.path.exists(fullpath):
        fullpath = open(fullpath,'r')
        jsondata=json.load(fullpath)
        if os.path.exists(tmpath):
            pass
        else:
            print("creating tmp directory")
            os.mkdir(tmpath)
        print(jsondata)
        print("from which source to target we are moving data...",jsondata['source'][-1], jsondata['target'][-1])
        print("1 try to change it as a query...",f"select {jsondata['cols'][0]},{jsondata['cols'][1]} from {jsondata['tablename']}" )
        finalsql=f"select {jsondata['cols'][0]},{jsondata['cols'][1]} from {jsondata['tablename']} where {jsondata['where']}"
        print("2 try to change it as a query...",finalsql )
        print("executing the sql in bigquery later",finalsql)
        fullpath.close()
        # block2 (seperate activity2)
        print("some independent activity")
    else:
        print("the file not exist",userinput)
except Exception as msg:
    print("exception occured",msg)
else:#if try is success
    print("entire try block is success without going to except block")
    srcpath=fullpath
    tgtpath=f"C:\\dataset1\\archival\\dma1.json"
    print(srcpath,tgtpath)
    shutil.move(srcpath,tgtpath)
finally:#i will run at any cost either try+except runs or try+else runs
    print("clean my vehicle")
    print("clean my disk post the operation is success/failed")
    tmpath = "C:\\dataset1\\tmp"
    shutil.rmtree(tmpath)

print("2. Types of exception handling - pre defined")
#There are different types of exceptions are available already in python
import os,shutil
try:
    a=10
    b=0
    int("hello")
    open("C:\\dataset1\\abcd")
    os.mkdir("C:\\dataset1\\tmp")
    print(a+b)
    print("hello")
    print(a/b)
except ValueError as e:
    print("value error", e)
except TypeError as e:
    print("pls provide the datatype as int because python is a strongly typed language",e)
    print("mail: maximum attempt of doing arthmetic is completed")
except ZeroDivisionError as e:
    print("pls provide the denominator properly",e)
except FileExistsError as e:
    print("sending mail to DE team")
    print("file already exists",e)
except FileNotFoundError as msg:
    print("mail to Source system: source data is not available, pls send it",msg)
except Exception as msg:
    print("i didn't know what exception occured, some common exception occured",msg)

print("3. Types of exception handling - user defined")
#There are different types of exceptions are available already in python
class IVRWrongOption(Exception):#inheritance
    print("code for disconnecting the ivr call")

try:
    airtel_callcenter:list=['bill','conn','ccrep']
    option_chosen=input("pls any one of the 3 options")
    if option_chosen in airtel_callcenter:
        print("take you further...")
    else:
        print("the expected option is not chosen, i am taking you out of the ivr as lot of queue is there, i am raising an exception")
        raise IVRWrongOption
except IVRWrongOption:
    print("user ivr connection disconnected")

print("3. Way of writing exception handling - Block level & Statement level")