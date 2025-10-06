1 task: 
a = input('write your name')
b = int(input('write your year of birth'))
c = 2025 - b

print(f'hello {a}, you are {c} years old')


2 task:
txt = 'LMaasleitbtui'
car1 = txt[0::2]
car2 = txt[1::2]

print(f'your first car name is {car1}, the second car name is {car2}')

3 task:

txt = 'MsaatmiazD'
car1 = txt[0::2]
car2 = txt[1::2]
t = car2[::-1]

print(f'your first car name is {car1}, the second car name is {t}')



4 task:

txt = "I'am John. I am from London"
r = txt[21::]

print(f'the residence name is {r}')


5 task:

a = input('give your strint i will reverse it')

b = a[::-1]


print(f'your string reverse version is {b}')

6 task:
a = input('input your text i will count vowels')
vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
count = 0
for letter in a:
    if letter in vowels:
        count += 1
print(f'number of vowels is {count}')

7 task:

a = input("Input your numbers, I will choose the highest: ")

numbers = [float(x) for x in a.split()]

maxx = max(numbers)

print(f"The max number is {maxx}")

8 task:

a = input('input your word i will check if it is polidrome')
b = a[::-1]

if a == b:
    print(f'yes your word {a} is polindrome')
else:
    print(f'no your word {a} is not polindrome')

9 task: 
email = input("Enter your email address: ")

if "@" in email:
    domain = email.split("@")[1]
    print(f"The domain of your email is: {domain}")
else:
    print("Invalid email address. Please include '@'.")

10 task:

import random
import string

letters = string.ascii_letters  
digits = string.digits           
symbols = string.punctuation     
all_chars = letters + digits + symbols

length = int(input("Enter password length: "))

password = ''.join(random.choice(all_chars) for _ in range(length))

print(f"Your random password is: {password}")






