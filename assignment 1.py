#Task1
a = input(' ban ten gi')
print('xin chao',a)

#task2
a= float(input('radius of the circle:'))
b = 2*a*3.14
print ('the circumference of the circle is', round(b))

#task3
a= float(input('length of the rectangle:'))
b= float(input('width of the rectangle:'))
if a > b: 
  c= (a+b)*2
  d= a*b
  print('the area of the circle is', c)
  print('the perimeter of the circle is', d)
else:
  print("no value")
  
#task4
a= int(input('first number:'))
b= int(input('second number:'))
c= int(input('third number:'))
sum= a+b+c
product = a*b*c
average= sum/3
print('the sum is', sum)
print('the product is', product)
print('the average is', average)

#task5
a= float(input('enter talents'))
b= float(input('enter pounds'))
c= float(input('enter lots'))
total = a*20*32*13.3+b*32*13.3+c*13.3
kilogram= int(total/1000)
gram= total- kilogram*1000
print(f"kilogram is {kilogram} and gram is  {gram}")

#task6
import random
a1= random.randint(0,9)
a2= random.randint(0,9)
a3= random.randint(0,9)

b1= random.randint(1,6)
b2= random.randint(1,6)
b3= random.randint(1,6)
b4= random.randint(1,6)

print(f"lock 1 is:{a1},{a2},{a3}")
print(f"lock 2 is:{b1},{b2},{b3},{b4}")








