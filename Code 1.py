from cmath import pi


pi
r = float(input("radius :"))
print("Area for radius "+str(r)+str(pi*r**2))



A = input("Enter Filename : ")
B = A.split(".")
print("Extension : "+ B[-1])
