def read_data_from_db():
    print("Reading data from database using some logics...")
    return [(1,'irfan'),(2,'inceptez')]

def read_data_from_fs(somefilepath):
    print("Reading data from file using some logics...")
    return {1:10,2:20}

#main check
if __name__ == "__main__":
    #main is the starting/entry point of any python program
    #it safeguard this program from unwanted execution
    print("util program")
    #print(read_data_from_db())
    #print(read_data_from_fs(""))

