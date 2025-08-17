
a = int(input("What is a?  "))
b = int(input("What is b?  "))
c = int(input("What is c?  "))

root1 = (-b + (b**2 - 4 * a * c)**(1/2))/(2 * a)
root2 = (-b - (b**2 - 4 * a * c)**(1/2))/(2 * a)

if isinstance(root1, complex):
    print("The first root is an imaginary number.")
else:
    print("The first root is",root1, ".")
   
if isinstance(root2, complex):
    print("The second root is an imaginary number.")
else:
    print("The second root is",root2, ".")
    
    
    