1. 
ls = ['apple, banana, cherry, watermelon, pineapple']
ls[2]

2.
ls1 = ['malibu', 'amerika']
ls2 = ['jentra', 'usa']
ls1 += ls2
ls1

3. 
ls3 = ['mercedes', 'bmw', 'hyundai', 'kia', 'chevrolet']
first = ls3[0]
middle = ls3[2]
last = ls3[-1]
ls4 = [first, middle, last]
print(ls4)

4.
film = ['avengers', 'focus', 'tor', 'polat', 'legacy']
tl_films = tuple(film)
type(tl_films)

5. 
cities = [
    "London",
    "Paris",
    "New York",
    "Tokyo",
    "Berlin",
    "Madrid",
    "Rome",
    "Toronto",
    "Sydney",
    "Dubai"
]

if 'Paris' in cities:
    print('Yes Paris in the cities list')
else:
    print('No Paris is not in the cities list')

6.
new_list = [1, 2, 3, 4, 5, 6]
copy_list = new_list.copy()

copy_list

7. 

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers[0], numbers[7] = numbers[7], numbers[0]
numbers

8. 
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
slice_tpl = tpl[3:8]
print(slice_tpl)


9. 
colors = ['yellow', 'red', 'blue', 'black', 'red', 'green', 'blue']
colors.count('blue')


10. 
tples = [
'bird',
'zebra',
'lion',
'tiger']

tples.index('lion')

11.
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
tpl1 += tpl2
tpl1

12. 
mlist = [1,2,3,4,5]
mtpl = (1,2,3,4,5)
len(mlist)
len(mtpl)

13. 
tpl = (1,2,3,4,5,6,7)
mlist = list(tpl)
mlist


14. 
tpl = (1,2,3,4,5,6,7,8,9,10)
minimum = min(tpl)
maximum = max(tpl)
print(f'the min amount is {minimum}, the max amount is {maximum} in tuple')

15.

tpl = ('great', 'good', 'time', 'watch')
tpltest = tpl[::-1]
tpltest






























