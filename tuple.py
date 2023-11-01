#tuple = ()
#print(tuple)
list =(1,4,8)
print("tuple using list:")
print(tuple(list))
tuple1 = (10,20,300)
tuple2 = ('python','algorithm')
tuple3 = (tuple1,tuple2)
print("tuple using nested tuple:",tuple3)
##Tuple using loop
tuple ='circket'
n=7
print("tuple using loop\n")
for  i in range(int(n)):
             tuple=(tuple,)
             print(tuple)
Tuple1=(14,121,145)
Tuple2=('python','data','science')
Tuple3=Tuple1+Tuple2
print("Tuple1: ",Tuple1)
print("Tuple2: ",Tuple2)
print("After concatenation: ",Tuple3)
## Slicing Tuples
Tuple4=('pythonfordatascience')
print("After removal of first element:")
print(Tuple4[1:])
print("After the sqeunce is reversed:")
print(Tuple4[::-1])
print("printing element in range:")
print(Tuple4[4:10])
list =(1,4,8)
print(list.index(8))