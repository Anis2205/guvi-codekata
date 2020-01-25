def Add():
    val=input("type the value")
    a.append(val)
def Delete():
    val=input("enter the element to delete")
    a.remove(val)
def Edit():
    val=input("enter the name of element that you want to edit")
    b=a.index(val)
    a.remove(val)
    val=input("insert the new value")
    a.insert(b,val)
def Display():
    for i in a:
        print(i)
a=[]
ch='y'
while  ch=='y':
   print("enter the option")
   op=input("1.Add 2.Delete 3.Edit 4.Display")
   if op=='Add':
      Add()
   elif op=='Delete':
      Delete()
   elif op=='Edit':
      Edit()
   elif op=='Display':
      Display()
   ch=input("press y to continue and n to exit ")




