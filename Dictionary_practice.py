
# def my_func(x):
#     return 5 * x

# # print(my_func(5))

# def recursion(i):
#     for x in range(i):
#         print(i)
#         if (x > 0):
#             val = x + 1
#             print(val)
#         return
# recursion(5)


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
# tri_recursion(5)

# x = 5
# while (x < 10):
#     print(x)
#     x += 1

# for x in "mayank":
    # print(x)

# a = 2
# b = 330
# print("A") if a > b else print("B")


a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
for i in [0,1,2]:
  pass