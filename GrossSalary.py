salary=int(input("enter the basic salary"))
if(salary<10000):
   HRA=(salary*67)/100
   DA=(salary*73)/100
elif(salary<20000):
   HRA=(salary*69)/100
   DA=(salary*76)/100
else:
   HRA=(salary*73)/100
   DA=(salary*89)/100
gross_salary = HRA + DA + salary
print(gross_salary)