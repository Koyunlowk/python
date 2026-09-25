
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

