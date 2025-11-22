#functions (75%) fbp- pkg.subpkg.module.functions
#class/functions (25%) oops+fbp-pkg.subpkg.module.class.functions

#class is a main program that holds the subprograms
#xls class (template/blueprint) holds subprograms (functions) (tabs)
class xls:
    def tab1(self):
        pass
    def tab2(self):
        pass

class prod_cost:
    def installation_cost(self):
        installation_cost=100+10
        return installation_cost
    def total_cost(self):
        total_cost=self.installation_cost()
        return total_cost

mohan_open=xls()
print(mohan_open.tab1())
karthick_open=xls()
print(karthick_open.tab1())