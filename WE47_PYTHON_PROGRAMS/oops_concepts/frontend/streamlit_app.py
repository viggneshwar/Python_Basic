from oops_concepts.backend.main import load_data,search_data,read_data_from_fs
#Exact difference between import and from import to avoid conflict/ambiguity we use import
#from oops_concepts.backend.utils import *
#from oops_concepts.frontend.utils import *
#or
#import oops_concepts.backend.utils as be
#import oops_concepts.frontend.utils as fe
#print(read_data_from_db())
#print(fe.abcd)
#print(be.abcd)

print("some one clicks the button in the FE, call the below funciton, then fit the data in the ui with the result")
user_click=input("press a button in the FE")
if user_click=='load_db_data':
    print("calling load data function")
    ui_data=load_data('db')
else:
    ui_data =read_data_from_fs('C:\\dataset\\a.json')
print('output in the frontend',ui_data)
#print(somevariable)