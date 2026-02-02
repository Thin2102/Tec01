#task 1
num = 1
while num <=1000:
    if num %3 ==0:
        print (num)
    num +=1

#task 2
while True:
    a = float(input('enter a number inches to centimeters:'))
    b = a*2.54
    if a <=0:
        print('must be positive number')
        break
    print(b)

#task 3
c = None
d= None
while True:
    a = input('enter a number: (press enter to quit)')
    if a =="":
        break
    b = float(a)

    if c is None or b > c:
        c = b
    if d is None or d > b:
        d = b
if c is not None:
    print("largest number is ", c)
    print("smallest number is ", d)
else:
    print('no number was entered')

#task 4
import random
i = random.randint(1,10)
while i > 0:
    a= int(input('enter a number from 1 to 10: '))
    if a =="":
        print('game end')
        break
    if a > i:
        print('lower')
    elif a < i:
        print('higher')
    else:
        print('correct answer')
        break

#task 5
c=0
while c <5:
    a = str(input('enter username: '))
    b = str(input('enter password: '))
    if a =="python" and b=="rules":
        print("welcome")
        break
    else:
        print("wrong answer")
    c+=1
    if c ==5:
        print("access denied")

#task 6
def get_middle(s):
    n = len(s)
    if n % 2 == 0:
        return s[n//2 - 1] + s[n//2]
    else:
        return s[n//2]
text = input('enter a string: ')
result = get_middle(text)
print("the middle is",result)

#task 7
def acronym(phrase):
    words=phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result
text = input('enter a string:')
print(acronym(text))











