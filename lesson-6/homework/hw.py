
1 exercise

def modify_string(s):
    vowels = 'aeiouAEIOU'
    res = ''
    i = 0
    while i < len(s):
        res += s[i]
        if (i + 1) % 3 == 0 and i != len(s) - 1:  
            if s[i] in vowels or (i + 1 < len(s) and s[i + 1] == '_'):
                if i + 1 < len(s) - 1:
                    res += s[i + 1] + '_'
                    i += 1
            else:
                res += '_'
        i += 1
    return res

print(modify_string("gcfycycgvouhlbnjkll"))



2 exercise

n = int(input('enter your number'))

for x in range(0, n):
    if n > 20:
        print('Your number is greater than 20')
        break
    else:
        print(x ** 2)


3 exercise

i = range(0, 11)  
x = 0              

while x in i:      
    print(x)
    x += 1    


4 exercise


n = 5 

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print() 



5 exercise

n = int(input("enter your number: "))
total = 0

for i in range(1, n + 1):
    total += i

print(total)


6 exercise

n = int(input("Enter your number: "))

for i in range(1, 11):
    print(n * i)


7 exercise

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break         
    if num > 150:
        continue        
    if num < 50:
        continue        
    print(num)



8 exercise

number = 75869

len(str(number))


9 exercise

n = 5

for i in range(n, 0, -1):      
    for j in range(i, 0, -1):   
        print(j, end=" ")
    print()  # новая строка после каждого ряда



10 exercise


list1 = [10, 20, 30, 40, 50]
list1.reverse()
for x in list1:
    print(x)

11 exercise

x = range(-10, -0)

for i in x:
    print(i)


12 exercise


for i in range(5):
    print(i)
else:
    print("Done!")


13 exercise


for i in range(25, 51):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)

14 exercise



n = 10
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b






15 exercise
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is", fact)





16 exercise


list1 = [1, 1, 2]
list2 = [2, 3, 4]  


uncommon = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
print(uncommon)
