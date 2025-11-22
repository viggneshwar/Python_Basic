from oops_concepts.backend.izutils import *
def load_data(typeofsource):
    '''this fun help us to laod data from db'''
    if typeofsource == 'db':
        df=read_data_from_db()
    else:
        df=read_data_from_fs()
    return df

def search_data(search_term):
    print("some logic realted to search some data")

somevariable='xyz value'
