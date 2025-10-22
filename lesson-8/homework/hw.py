# 1. Handle ZeroDivisionError
try:
    num = int(input("Введите число: "))
    result = num / 0  # Деление на ноль вызовет исключение
except ZeroDivisionError:
    print("Ошибка: деление на ноль невозможно!")
else:
    print("Результат:", result)
finally:
    print("Программа завершена.")

# ---------------------------------------------
# 2. Handle ValueError for invalid integer input
try:
    num = int(input("Введите целое число: "))
except ValueError:
    print("Ошибка: это не целое число!")
else:
    print("Результат:", num)
finally:
    print("Программа завершена.")

# ---------------------------------------------
# 3. Handle FileNotFoundError
try:
    address = input("Введите адрес файла: ")
    file = open(address, "r")
except FileNotFoundError:
    print("Ошибка: файл не найден. Введите корректный адрес файла.")
else:
    print("Содержимое файла:")
    print(file.read())
    file.close()
finally:
    print("Программа завершена.")

# ---------------------------------------------
# 4. Handle TypeError for non-numeric input
try:
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")

    if not (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()):
        raise TypeError("Ввод должен быть числом!")

    num1 = float(num1)
    num2 = float(num2)
    result = num1 + num2

except TypeError as e:
    print("Ошибка:", e)
else:
    print("Результат:", result)
finally:
    print("Программа завершена.")

# ---------------------------------------------
# 5. Handle PermissionError
try:
    with open("example.txt", "r") as file:
        print(file.read())
except PermissionError:
    print("Ошибка: нет прав доступа к файлу.")

# ---------------------------------------------
# 6. Handle IndexError
my_list = [1, 2, 3]
try:
    index = int(input("Введите индекс элемента: "))
    print(my_list[index])
except IndexError:
    print("Ошибка: индекс вне диапазона списка.")

# ---------------------------------------------
# 7. Handle KeyboardInterrupt
try:
    num = int(input("Введите число: "))
    print("Вы ввели:", num)
except KeyboardInterrupt:
    print("\nВвод был прерван пользователем.")

# ---------------------------------------------
# 8. Handle ArithmeticError
try:
    x = 10
    y = int(input("Введите делитель: "))
    result = x / y
except ArithmeticError:
    print("Произошла арифметическая ошибка.")
else:
    print("Результат деления:", result)

# ---------------------------------------------
# 9. Handle UnicodeDecodeError
try:
    with open("example.txt", "r", encoding="utf-8") as file:
        print(file.read())
except UnicodeDecodeError:
    print("Ошибка кодировки файла.")

# ---------------------------------------------
# 10. Handle AttributeError on list operation
my_list = [1, 2, 3]
try:
    my_list.appendd(4)  # Ошибка: метода appendd не существует
except AttributeError:
    print("Ошибка: такого метода не существует для списка.")

# ---------------------------------------------
# 11. Read entire text file
with open("example.txt", "r") as file:
    content = file.read()
print(content)

# ---------------------------------------------
# 12. Read first n lines
n = int(input("Сколько строк читать? "))
with open("example.txt", "r") as file:
    for i in range(n):
        print(file.readline().strip())

# ---------------------------------------------
# 13. Append text to a file and display
text = input("Введите текст для добавления: ")
with open("example.txt", "a+") as file:
    file.write(text + "\n")
    file.seek(0)
    print(file.read())

# ---------------------------------------------
# 14. Read last n lines
n = int(input("Сколько последних строк читать? "))
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line.strip())

# ---------------------------------------------
# 15. Read file into a list
with open("example.txt", "r") as file:
    lines_list = file.readlines()
print(lines_list)

# ---------------------------------------------
# 16. Read file into a variable
with open("example.txt", "r") as file:
    content = file.read()
print(content)

# ---------------------------------------------
# 17. Read file into an array (list)
with open("example.txt", "r") as file:
    array = [line.strip() for line in file]
print(array)

# ---------------------------------------------
# 18. Find longest words
with open("example.txt", "r") as file:
    words = file.read().split()
longest_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == longest_length]
print("Самые длинные слова:", longest_words)

# ---------------------------------------------
# 19. Count number of lines
with open("example.txt", "r") as file:
    line_count = sum(1 for _ in file)
print("Количество строк:", line_count)

# ---------------------------------------------
# 20. Word frequency count
with open("example.txt", "r") as file:
    words = file.read().split()
word_count = Counter(words)
print(word_count)

# ---------------------------------------------
# 21. Get file size
size = os.path.getsize("example.txt")
print("Размер файла:", size, "байт")

# ---------------------------------------------
# 22. Write a list to a file
my_list = ["apple", "banana", "cherry"]
with open("example.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")

# ---------------------------------------------
# 23. Copy file contents
with open("source.txt", "r") as src, open("dest.txt", "w") as dst:
    dst.write(src.read())

# ---------------------------------------------
# 24. Combine lines from two files
with open("file1.txt") as f1, open("file2.txt") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

# ---------------------------------------------
# 25. Read a random line
with open("example.txt") as file:
    lines = file.readlines()
print(random.choice(lines).strip())

# ---------------------------------------------
# 26. Check if file is closed
f = open("example.txt")
print("Файл закрыт?", f.closed)
f.close()
print("Файл закрыт после close?", f.closed)

# ---------------------------------------------
# 27. Remove newline characters
with open("example.txt", "r") as file:
    lines = [line.strip() for line in file]
print(lines)

# ---------------------------------------------
# 28. Count words in a text file
with open("example.txt", "r") as file:
    text = file.read()
word_count = len(text.split())
print("Количество слов:", word_count)

# ---------------------------------------------
# 29. Extract characters into a list
chars = []
for filename in ["file1.txt", "file2.txt"]:
    with open(filename, "r") as file:
        chars.extend(list(file.read()))
print(chars)

# ---------------------------------------------
# 30. Generate 26 text files A.txt to Z.txt
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write("")

# ---------------------------------------------
# 31. Create alphabet file with n letters per line
n = int(input("Сколько букв на строку? "))
letters = string.ascii_uppercase
with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        file.write(letters[i:i+n] + "\n")
