import math
from ftplib import print_line

name='Gilik'
age=2.1
age1 = 2
print(f'Hello, my name is {name} and my age is {age // age1}')

# r=10
# print(f'π * {r * 2}')

aa = 3
bb = '12t'

print(f'{aa * bb}')



if bb.isdigit():
    print('Good')
else:
    print('Bad')

if bb.find('te') != -1:
    print("GGGGG")
elif bb.find('12') > -1:
    print('sssssss')


print(len(bb))
print(bb.isdigit())

print(name[0])

for x in range(1, 11, 1):
    print_line(x ** 2)

for x in range(1, 11, 1):
    if x ** 2 == x * 4:
        print (x)
        break

for x in range(1, 11, 1):
    if (x ** 2) % 7 == 0:
        print(f'No remains fo 7: {x}')
    if str(x).find('7') > -1:
        print(f'Contains 7: {x}')

list_string = ['aaaa','bbbb','cccc','dddd', 14]
list_string.insert(2, 11)
print(f"Here {list_string[:]}")

for x in list_string:
    print(f'Yeah {x}')

a=''
for x in range(1, len(name), 1):
    a += name[x - 1]
    print(a)


list1=[1,2,3,4,32,6,17] # Define list
B = 5 in list1 #False
A = 1 in list1 #True
print (A,B, 'gg')
print(list1[0])
list1.reverse()
print("Rev:", list1[0])
list1.sort(reverse = True)
print("Sort:", list1[0])


summ = 0
ind = 0
for x in list1:
    ind += 1
    if x > 10:
        print(x)

    summ += x

print (f"Sum: {summ}")
print (f"Ave: {summ / ind}")
print (f"Ave: {summ / len(list1)}")
print ("Ave:", summ / len(list1))

list_cities = ["London", "Pari", "a "]
for y in list_cities:
    if len(y) >= 4:
        print(y)
u = 36
print(u)
U = 'lk'
print(u)

my_dict = {'first_name':'Gil',
           'last_name':'Shalev'}
print(my_dict['first_name'])
print(my_dict.get('first_name'))
my_dict['age'] = 12
print(len(my_dict))
my_dict.setdefault("age", 33)
print(my_dict['age'])

print(math.pi)
print(int(math.sqrt(4)))
print(math.isqrt(4))

str1= 'hHipo'
str1 = str1.replace("h", "g", 2)
print(str1.lower())

def my_sum(num1, num2):
    return num1 + num2

print(my_sum(2, 5))

a = 9
b = 8
c = 7
print('Value is: ' + str(a))
print('Value is:', a)
print(f'Value is: {a}')


def check_cities(list_cities1):
    i = -1
    names=[]
    for x1 in list_cities1:
        if x1.find(' ') > -1 or x1[0].islower() == False:
            i += 1
            names.insert(i, x1)

    print(list_cities1[:])
    return names

out_names = check_cities(list_cities)
print(out_names)
print(list_cities)

def ret_check():
    arr1 = ["we", "you"]
    # return "d", "k"
    return arr1

var1, var2 = ret_check()
print(var1)
print(var2)

var3 = ["dd", "kk"]
var3 = ret_check()
print(var3[:])
print(var3[0])
print(list_cities[:])