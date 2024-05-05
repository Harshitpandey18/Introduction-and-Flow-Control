print("Shapes:\n1. Circle\n2. Rectangle\n3. Square")
x=int(input("Select a number from the given list: "))
if(x==1):
    r=int(input("Enter radius of the circle: "))
    area=3.14*r*r
    peri= 2*3.14*r
    print("The area of circle is", area)
    print("The perimeter of circle is", peri)
elif(x==2):
    l=int(input("Enter length of Rectangle: "))
    b=int(input("Enter breadth of Rectangle: "))
    area=l*b
    peri=2*(l+b)
    print("The area of Rectangle is", area)
    print("The perimeter of the Rectangle is", peri)
elif(x==3):
    s=int(input("Enter the side of the Square: "))
    area= s*s
    peri= 4*s
    print("The area of Square is", area)
    print("The perimeter of the Square is", peri)
else:
    print("wrong choice")

