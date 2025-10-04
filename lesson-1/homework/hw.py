Given a side of square. Find its perimeter and area.
Given diameter of circle. Find its length.
Given two numbers a and b. Find their mean.
Given two numbers a and b. Find their sum, product and square of each number.


1. a = int(input('give a first length'))
  b = int(input('give a second length'))

  P = 2 * (a + b)
  S = a * b

  print(f'Perimetr: {P}, Square: {S}')


2. a = float(input('Give the diametr a circle in mm'))

   Length = a * 3.14

   print(f'Length of circle: {round(Length, 2)} mm')

3. a = int(input('give the first valur'))
   b = int(input('give the second value'))

   C = (a + b) / 2

   print(f'the mean of two values equal to {round(C, 2)}')

4. a = int(input('give the first valur'))
   b = int(input('give the second value'))

   A = a + b
   B = a * b
   C = a * a
   D = b * b

print(f"""
The sum is equal to {A}
The product is equal to {B}
The square of the first value is equal to {C}
The square of the second value is equal to {D}
""")

