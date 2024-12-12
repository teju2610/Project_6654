project=int(input("enter the project score"))
internal=int(input("enter the internal score"))
external=int(input("enter the external score"))
if project>=50 and internal>=50 and external>=50:
   pro=(project*70/100)
   inter=(internal*10/100)
   exter=(external*20/100)
   total=pro+inter+exter
   print(total)
   if total>=90:
       print("A grade")
   elif total>80:
       print("B grade")
   else:
       print("c grade")
else:
   if(internal<50):       
       print("failed in internal",internal)
   if(external<50):
       print("failed in external",external)
   if project<50:
       print("failed in project",project)