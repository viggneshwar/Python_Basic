#EXCEPTION HANDLING
#Understanding of Exception: what? unexpected event occured while executing a program (non zero exit), if we have a control/handler/mitigation for an exception then it is exception handler
#exception handler blocks (try,except,else,finally)
#important blocks that we use mostly are (try,except)
#mandatory combination of using blocks (try+except or try+finally)
#else block is optional everywhere

#Types of Exception: Predefined ()
# & Userdefined/CustomExceptions ()

#WITHOUT THINKING ABOUT ANYTHING ELSE, JUST ONLY ADD THIS LINE OF CODE IN YOUR ANY OF YOUR PROGRAM
#TO FULFIL EXCEPTION HANDLING MINIMUM
#i am writing a normal program like this...
a=10
b=20
print(a/b)
#how can i add exception handling in this program to make it more standard (add try and except block)
try:#minimum this line
    a = 10
    b = 0
    print(a / b)
    print("program completed successfully")
except Exception as errdesc:#minimum this line
    print("some exception occured, check the error description here... ",errdesc)


print("1. Fundamendals of Exception Handling")
print("What? When an unexpected event occured, how to handle that without making the program abruptly terminated")
print("Exception handling blocks: try, except, else & finally")
#Analogical/layman understanding
'''
try:#main program that i want to run
    i went to a shop yesterday to have burger (succeed will take else)/(failure will take to except)
except:#if main program failed then run this except block
    because shop is closed, i taken kids to a different shop (copper kitchen dinner)
else:#if main program succeeded then run this else block
    i might have had soft drink
finally:#i have to do this at any cost (success/failed)
    i came home and locked my car and main gate
'''

#try: The main (mandatory) block where the main program is writtened
#except: The exception handler (optional) block where the handler program is writtened
#else: The else (optional) block of except block (if try is success then go to else, if except is success then don't go to else)
#finally: This is a default block (optional) that runs always at any cost (whether try/except/else is success/fail
#strategic : 2 important things we are going to learn (1. different filesystem operations + 2.exception handling)
#What we are learning in this one strategic program?
#Different fs operations using python: open, check for existance, close, parse files in json format,
#move of file (archival), removal of directory (purging)
#Usage of all blocks in exception handling in python...
#strategic program
try:
    import json
    import os
    import shutil
    initialval=1
    finalvalue=3
    while finalvalue>=initialval:
        filename=input("enter the filename")
        archivepath = "C:\\dataset2\\archive\\"
        location="C:\\dataset2\\"
        loc_file=location+filename
        if os.path.exists(loc_file):#graceful way of writing program
            file_open_from_disk_mem=open(loc_file)
            json_file = json.load(file_open_from_disk_mem)
            print("file opened successfully")
            # file_open_from_disk_mem=open("C:\\dataset2\\dma.json")
            print("parsing the file")
            all_lst_cols = json_file["cols"]
            col1 = all_lst_cols[0]
            col2 = all_lst_cols[1]
            tabname = json_file['tablename']
            sqlquery = f"select {col1},{col1} from {tabname}"
            list_source_user_chosen = json_file['source']
            second_source = list_source_user_chosen[1]
            print(f"run this query in the source database of {second_source} ", sqlquery)
            break
        else:
            print("you have more options to try is",finalvalue-initialval)
            initialval+=1
            continue
except Exception as exceptiondesc:#handler block
    print("Some exception occured",exceptiondesc)
    file_open_from_disk_mem.close()
else:
    print("As my main try block of generating sql is completed, i am going to backup the file from source to archive path")
    #location = "C:\\dataset2\\"
    #loc_file = location + filename
    #file_open_from_disk_mem = open(loc_file)
    file_open_from_disk_mem.close()
    shutil.move(loc_file,archivepath)
finally:
    print("Whether my try block is completed or not, I am going delete if any tmp folders are created by our process")
    tmppath = "C:\\dataset2\\tmp\\"
    if os.path.exists(tmppath):
        shutil.rmtree(tmppath)

#file processing in any environment
'''
/source/file_today.txt
process
move /source/file1.txt /archive/file.txt #by doing this i am giving way to new files
rm /archive/file.txt #purge
'''

print("2. Types of exception handling - pre defined")
#There are different types of exceptions are available already in python
try:
    #open("C:\\dataset1\\hellofile")
    print(1/1)#arithmetic/zero divide error
    #print(hello)#nameerror
    print(int(input("pass something")))
    #print(xyz)
#Error
except FileNotFoundError as e:#predefined exception
    print("file not found error",e)
except NameError as e:
    print("name not found error",e)
except ValueError as e:
    print("value error",e)
    print(int(input("pass only number")))
except ArithmeticError as e:#predefined exception programs can be used to manage exception very much specific
    print("Arithmetic error",e)
except Exception as e:#common exception
    print("some common error occured",e)

print("3. Types of exception handling - user defined/custom")
class DeptCheckError(Exception):
    print("expecting only the required departments of IT,HR,MKT")

try:
    deptlist = ["IT", "HR", "MKT"]
    userdept = input("enter the department")
    if userdept not in deptlist:
        raise DeptCheckError("**dept not found**")
    else:
        print("user choosen the expected department", deptlist.count(userdept))
except DeptCheckError as e:
    print("exception occured", e)
except Exception as e:
    print("some common error occured", e)

print("4. Way of writing exception handling - Block level & Statement level")
try:#block level exception, for dependent block/statements of code
    print(1/0)#line1 fails it will fail the entire block of code
    print("line2 will not run")
    print("line3 will not run")
except Exception as e:
    print("exception occured", e)

try:#statement level exception, for independent block/statements of code
    print(1/0)#line1 fails it will fail that particular line/statement alone, without affecting other statements
except Exception as e:
    print("exception occured in statement1", e)
try:
    print("line2 will run")
    print(1 / 0)
except Exception as e:
    print("exception occured in statement2",e)
try:
    print("line3 will run")
    print(1 / 0)
except Exception as e:
    print("exception occured in statement3",e)