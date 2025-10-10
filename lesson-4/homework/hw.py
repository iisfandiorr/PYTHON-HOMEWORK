1 task

sample_dict = {'Name': "Daniel", 'last_Name': "trevor", 'Adress': 'NY', 'email': 'daniel@mail.ru'}
sorted(sample_dict)


2 task

sample_dict = {0: 10, 1:20}
sample_dict.update({2: 30})
print(sample_dict)


3 task
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic1.update(dic2)
dic1.update(dic3)
dic4 = dic1
print(dic4)


4 task

n = 5
square_dict = {}

for x in range(1, n + 1):
    square_dict[x] = x * x

print(square_dict)


5 task

n = 15
square_dict = {}

for x in range(1, n+1):
    square_dict[x] = x * x
print(square_dict)




6 task

sample_set = {1, 2, 3, 4, 5, 6}
type(sample_set)


7 task

x = 40

if x > 30:
    print('x greater than 30')
elif x == 30:
    print('x equal to 30')
else:
    print('x smaller than 30')

8 task

sample_set.add(7)
print(sample_set)

9 task

sample_set.remove(7)
print(sample_set)


10 task

sample_set.discard(10)
print(sample_set)


