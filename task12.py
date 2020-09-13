import math
r=float(input('enter radius:'))
area = math.pi * r * r
print("area of the circle is:%2f" %area)
print("second task")

#filename
fn=input('input the filename:')
f = fn.split(".")
print("the extension of the file is:")
if f[-1]=="py":
   print("python")
