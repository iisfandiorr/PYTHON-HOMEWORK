1 task

n = int(input("Enter your number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("False")
            break
    else:
        print("True")
else:
    print("False")


2 task

def digit_sum(k):
    total = 0
    for digit in str(k): 
        total += int(digit)
    return total


print(digit_sum(45))



3 task

def quater(N):
    k = 1
    while 2 ** k <= N:
        print(2 ** k, end=" ")
        k += 1

print(quater(45))

