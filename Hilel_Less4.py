# Lesson 4 task 1
my_string = "43 більше ніж 34 але менше ніж 56"
print(sum(int(i) for i in my_string.split() if i.isdigit()))

# Lesson 4 task 2
my_list = ["агония", "абзац", "Артем", "Андрей",
           "аккум", "Абрам", "Апостол", "Август"]
my_new_list = []
[my_new_list.append(i) for i in my_list if i.lower().startswith('а')]
print(my_new_list)

# Lesson 4  task3
my_list1 = ["name", 123, 321, 5, "style"]
my_list2 = [123, 321, 4, "world!", "cucumber"]
new_uniq_list = (list(set(my_list1) ^ set(my_list2)))
print(new_uniq_list)

# Lesson 4 task 4

my_new_lst = []
my_str = input()
if len(my_str) % 2 != 0:
    my_str += '_'
while len(my_str) > 0:
    my_new_lst.append(my_str[:2])
    my_str = my_str[2:]
print(my_new_lst)

# my_str = 'abcde'
# my_new_generated_list = []
# while len(my_str) > 1:
#     my_new_generated_list.append(my_str[:2])
#     my_str = my_str[2:]
#     if len(my_str) == 1:
#         my_new_generated_list.append(my_str[:2].ljust(2,'_'))
# print(my_new_generated_list)
