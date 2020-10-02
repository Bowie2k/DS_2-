# *** Множество (set) ***


# Особенности:
# - неупорядочнная коллекция 
# - нету индексов 
# - при создании автоматический удаляются все дублирующие объекты 


# *** создания множества ***

# первый способ 
my_set = {"a", "b", "c"}

# второй способ 
s = "hello"
my_list = [100,200, 300,100,200]

my_set_2 = set(my_list) 

# *** Добавление элементов ***

my_set.add(777)
my_set.add((12,23,36,45)) # добавляется только кортеж 

# *** удаление элементов ***

my_set = {10,20,30,40}

# my_set.remove(30)

# проблема при удалении 
# my_set.remove(50)

# решение проблемы 
my_set.discard(40)


# *** объединения множеств ***

users = {"John","Tom","Khristina"}
new_users = { "Bob","John","Kate"}

# users = users.union(new_users) # union позволяет создать новое множество и при этом сохранить исходные множества 
users_2 = users | new_users # короткий аналог union()
# users.update(new_users) # тоже самое что и union(), но новое множество создается внутри первой переменной 

# *** определенние пересечений ***

intersect_users = users.intersection(new_users)

# короткий аналог метода intersection()
intersect_users = users & new_users

# # *** определение разности *** 
# diff_users = users.difference(new_users) # разность только из первого множителя 

# короткий аналог метода difference()
# diff_users = users - new_users

# sd_users = users.symmetric_difference(new_users) # симметричная разность 

# print(diff_users)

import this