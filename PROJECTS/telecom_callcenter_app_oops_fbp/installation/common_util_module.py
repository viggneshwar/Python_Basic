#generic/common/framework developers
#class is a template/blueprint
#xlsheet(class) -> tabs (members) func/var

#Irfan sorry if I missed this part, we have declared as self.path=folder, why not folder=self.path
class FSOps():#class
    #xyz="static variable"
    def __init__(self,folder='C:\\somepath\\tmp'):#Default/parameterized/non-parameterized constructor
        self.path=folder#member variable/attribute
        self.xyz=100
    def read_file(self,file):#member function
        print(f"installation pkg read_file from {self.path}{file}")
        #self.file=file
    def write_file(self):#member function
        print("write_file")
    #print(xyz)
    @staticmethod
    def standalone():
        print("standalone")

class DBOps:#Non parameterized class
    def read_db(self):
        print("read_db")
    def write_db(self):
        print("write_db")
