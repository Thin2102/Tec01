#task 1
def Zander():
    while True:
        try:
         a = float(input("size of the zander:"))
         if a < 42 and a > 0:
             b = 42-a
             print ('release the fish back into the lake, centimeters below the size limit the caught fish',b)
             break
         elif a >=42:
             print('bring to ur home')

             break
         else:
             print('enter a positive number')
             continue
        except:
         print('please enter a positive number')

Zander()
#task 2
def cabinclass():
    while True:

            a = input("enter class of cabin:").upper()
            if a == 'LUX':
                print(' upper-deck cabin with a balcony.')
                break
            elif a =='A':
                print(' above the car deck, equipped with a window.')
                break
            elif a=='B':
                print(' windowless cabin above the car deck.')
                break
            elif a=='C':
                print('windowless cabin above the car deck.')
                break
            else:
                print('invalid cabin class')

cabinclass()

#task 3
def hemo():
    while True:
        try:
            a =input(" enter biological sex")
            b=float(input("hemoglobin value"))
            if a=="male":
                if b >=134 and b <=167:
                    print('normal hemoglobin ')
                elif b<134:
                    print('low hemoglobin ')
                else:
                    print('high hemoglobin ')
                break
            elif a=="female":
                if b >=117 and b <=155:
                    print('normal hemoglobin ')
                elif b<117:
                    print('low hemoglobin ')
                else:
                    print('high hemoglobin ')
                break
            else:
                print('invalid hemoglobin value')
        except:
            print('please enter a positive number')
hemo()

#task 4
def leapyear():
    a  = int(input("enter year:"))
    if a%4==0 and a%100==0 or a%400==0:
        print('leap year')
    else:
        print('not a leap year')
leapyear()

#task 5

def duongkinh():
    a = float(input("enter diameter pizza 1 in centimeters:"))
    b = float(input("enter price pizza 1:"))
    c = a/2
    d = b/((c*c*3.14)/10000)
def duongkinh2():
    x = float(input("enter diameter pizza 2 in centimeters:"))
    y = float(input("enter price pizza 2:"))
    z = x/2
    g = y/((z*z*3.14)/10000)
    
while True:
    try:
        X = duongkinh()
        Z = duongkinh2()

        if Z > X :
            print('should buy pizza 1')
            break

        elif Z==X:
            print('the same,can buy pizza1 or pizza2')
            break
        else:
            print('should buy pizza 2')
            break
    except:
        print('please enter a right value')













