from project_simple_callcenter_app1.installation_util.installation_cost import CostingClass
#As a developer, we can test the python program we developed
nujma_obj1=CostingClass(100)
hrs_of_installation=nujma_obj1.calculate_installtime('stb')
print(nujma_obj1.calculate_cost(hrs_of_installation))

soundar_obj2=CostingClass(200)
hrs_of_installation=soundar_obj2.calculate_installtime('router')
print(soundar_obj2.calculate_cost(hrs_of_installation))
