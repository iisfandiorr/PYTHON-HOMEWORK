import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self.diameter = 2 * radius 
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return math.pi * self.diameter


r = float(input("Введи радиус круга: "))
c = Circle(r)

print(f"Площадь круга = {c.area()}")
print(f"Периметр круга = {c.perimeter()}")



class Person:
    def __init__(self, name: str, country: str, date: int):
        self.name = name 
        self.country = country
        self.date = date 
    def age(self):
        return 2025 - self.date
    
a = Person('John', 'Usa', 2003)
a.age()




class calc:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    def plus(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
    
calc1 = calc(50, 40)

calc1.plus()
calc1.minus()
calc1.multiply()
calc1.divide()



import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

    def perimeter(self):
        return 3 * self.side


r = float(input("Введи радиус круга: "))
circle = Circle(r)
print(f"Площадь круга = {circle.area()}")
print(f"Периметр круга = {circle.perimeter()}")

s = float(input("Введи сторону квадрата: "))
square = Square(s)
print(f"Площадь квадрата = {square.area()}")
print(f"Периметр квадрата = {square.perimeter()}")

t = float(input("Введи сторону треугольника: "))
triangle = Triangle(t)
print(f"Площадь треугольника = {triangle.area()}")
print(f"Периметр треугольника = {triangle.perimeter()}")

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)
        else:
            print("Значение уже существует в дереве")

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)


bst = BinarySearchTree()
elements = [7, 3, 9, 2, 5, 8, 10]

for e in elements:
    bst.insert(e)

print("Поиск 5:", bst.search(5))   
print("Поиск 12:", bst.search(12)) 






class Stack:
    def __init__(self):
        self.items = [] 

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Стек пуст!"

    def is_empty(self):
        return len(self.items) == 0



print("=== Stack Example ===")
stack = Stack()
stack.push(10)
stack.push(20)
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print()



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


print("=== Linked List Example ===")
lst = LinkedList()
lst.insert(1)
lst.insert(2)
lst.insert(3)
lst.display()
lst.delete(2)
lst.display()
print()



class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name):
        self.items = [item for item in self.items if item["name"] != name]

    def total_price(self):
        return sum(item["price"] * item["quantity"] for item in self.items)


print("=== Shopping Cart Example ===")
cart = ShoppingCart()
cart.add_item("Яблоко", 2.5, 3)
cart.add_item("Банан", 1.5, 2)
print("Общая сумма:", cart.total_price())
cart.remove_item("Банан")
print("После удаления:", cart.total_price())
print()


class StackWithDisplay:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Стек пуст!"

    def display(self):
        print("Текущий стек:", self.items[::-1])

    def is_empty(self):
        return len(self.items) == 0


print("=== Stack with Display Example ===")
stack2 = StackWithDisplay()
stack2.push(5)
stack2.push(10)
stack2.push(15)
stack2.display()
stack2.pop()
stack2.display()
print()


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item) 

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) 
        return "Очередь пуста!"

    def is_empty(self):
        return len(self.items) == 0


print("=== Queue Example ===")
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print()












class bankaccount:
    def __init__(self, name: str, balance: int = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount
        return self.balance
    
    def get_balance(self):
        return f'Customer name is {self.name}, balance is {self.balance}.'






