# print('Lesson 3, task 1 and 2')
# print('Simply range!')
# print(*list(range(0,21)))
# print(*list(range(-10,11)))
# input('Just pause for continue please press enter')
# print('Number in cycle')
#
# n = int(input('Please enter the number you want in range: '))
# for i in range(1,n+1):
#     print(i,end=' ')
# print()
# print('reverse cycle, with adding step in range -1')
# for i in reversed(range(n,-n-1,-1)):
#     print(i,end=' ')
# print()
# print('just range from -10 to 11 normal step +1')
# for i in range(-10,11):
#     print(i,end=' ')
# print()
# print('While Cycle')
# n = -1
# while n < 20:
#     n+=1
#     print(n, end=" ")
# print()
# input('Just pause for continue please press enter')
# print('Lesson 3, task 3: '
#       'Ladder with numbers')
# n = int(input('Please enter the number: '))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()
# # print('multiplication table')
# # for i in range(1,11):
# #     for j in range(1,11):
# #         k = i*j
# #         print(k, end=' ')
# #     print()
# input('Just pause for continue please press enter')
print('additional task')
print('first ')
result = []
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 2, 4, 5, 3, 34, 5, 3]
for i in enumerate(data):
    if i[0] % 2 != 0:
        # if not i[0] % 2 == 0:
        result.append(i[1])
print(result)
print(f' Result like in screen with out []:', *result)

print('var2')
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 2, 4, 5, 3, 34, 5, 3]
a = len(data)
for i in range(1, a, 2):
    print(data[i], end=' ')
print()
print('Var 3')
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 2, 4, 5, 3, 34, 5, 3]
a = len(data)
for i in range(a):
    if i % 2 != 0:
        print(data[i], end=' ')
