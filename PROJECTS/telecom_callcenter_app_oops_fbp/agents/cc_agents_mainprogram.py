from telecom_callcenter_app_oops_fbp.installation.common_util_module import FSOps
#oops minimum concepts (class,members,self,obj,constructor)
#class - is a template or blueprint program contains related members func/variables/subclasses
#member - any var/funct/classes inside the class is a member
#self - Used to identify the given program as a member (it is the reserved first parameter)
#object - Memory Instance/Copy of a class
#Constructor () - Memory in which we  construct/instantiate a class is constructor
#Types of Constructor

nujma_datapath_obj1 = FSOps(folder="C:\\datapath1\\")#() represents the constructor
balaji_datapath_obj2 = FSOps("D:\\datapath2\\")#() represents the constructor
vivek_datapath_obj3 = FSOps()#() represents the default constructor

#soundar_dbdata_obj4=DBOps()#Non param constructor

#() - constructor, used to load the class in memory
#ram_obj - object (memory where class is loaded)
#ram_obj.read_file("c:")
nujma_datapath_obj1.read_file("file1.csv")
balaji_datapath_obj2.read_file("file1.csv")



