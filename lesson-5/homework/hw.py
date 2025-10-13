


1 task: 
while True:
    year_input = input("Please give the year: ")

    if not year_input.isdigit():
        print("Please enter only numbers.")
        continue

    if len(year_input) < 4:
        print("Year must be at least 4 digits.")
        continue

    year = int(year_input)
    break

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Yes, your year is a leap year!")
else:
    print("No, your year is not a leap year.")


2 task:
while True:
    n_input = int(input('Please enter your number: '))

    if n_input % 2 == 1:
        print('Weird')

    elif n_input % 2 == 0 and 2 <= n_input <= 5:
        print('Not Weird')

    elif n_input % 2 == 0 and 6 <= n_input <= 20:
        print('Weird')

    elif n_input % 2 == 0 and n_input > 20:
        print('Not Weird')

    else:
        print('Please enter a number from 1 to 100!')
    break



3 task:


a = int(input('Give first number'))
b = int(input("Give the second Number"))

def even_numbers(a, b):
    if a > b:
        return []
    elif a % 2 == 0:
        return [a] + even_numbers(a + 1, b)
    else:
        return even_numbers(a + 1, b)
    
print(even_numbers(a, b)) 



a = int(input('Give first number'))
b = int(input("Give the second Number"))

evens = [x for x in range(a, b + 1) if x % 2 == 0]

print(evens)  
