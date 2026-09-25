
# /    หาร
# //   หารเอาจำนวนเต็ม
# %    หารเอาเศษ
# **   ยกกำลัง
#
# 10 / 3   # 3.333...
# 10 // 3  # 3
# 10 % 3   # 1
# 10 ** 3  # 1000

#ใช้ตรวจเลขคู่เลขคี่
# x = int(input("เลข:"))
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
# if x != 10:
#     print("ture")
# else:
#     print("false")

i = 1

# while i <= 5:
#     print(i)
#     i += 1 # i = i + 1

# for i in range(5):
#     print(i)

# range(start, stop, step)

# numbers = [10, 20, 30]
#
# for x in numbers:
#     print(x)

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# numbers = [10, 20, 30, 40]
# print(numbers[0])
# print(numbers[1])
# print(len(numbers))
# print(numbers.append(50))
# print(numbers[2:4])
# print(numbers[:3])
# print(numbers[2:])

# def hello():
#     print("Hello")
# hello() #เรียกใช้
#
# def add(a, b):
#     return a + b
#
# print(add(10, 20))
# result = add(10, 20)
# print(result)
# ans = result + 20 # สามารถนำไปใช้ต่อได้
# print(ans)
#
# def course_generate(): #การสร้าง object
#     yield "C"
#     yield "C++"
#     yield "Java"
#     yield "Python"
#
# course = course_generate()
# for x in course:
#     print(x)
#
# student = {
#     "name": "Bank",
#     "age": 19,
#     "major": "IT"
# }
# print(student["name"])
# student["age"] = 20 # เพิ่ม/แก้ Dictionary
# student["height"] = 167
# del student["height"]

def course1(y):
    print("You are interested in", y)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print("Hello",self.name)
s1 = Student("Bank", 19)
s1.say_hello()

try:
    x = int(input("Enter number: "))
except ValueError:
    print("Please enter a number")

Pattern 1 — นับ
count = 0

for x in data:
    if condition:
        count += 1
Pattern 2 — หาผลรวม
total = 0

for x in data:
    total += x

Pattern 3 — หาค่าสูงสุด
maximum = data[0]

for x in data:
    if x > maximum:
        maximum = x

Pattern 4 — หาค่าต่ำสุด
minimum = data[0]

for x in data:
    if x < minimum:
        minimum = x

Pattern 5 — ค้นหา
found = False

for x in data:
    if x == target:
        found = True
        break

Pattern 6 — กรองข้อมูล
for x in data:
    if condition:
        print(x)

Pattern 7 — Function

ถ้าทำอะไรซ้ำ ๆ:

def function_name(parameters):
    # process
    return result