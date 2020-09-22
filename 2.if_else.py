# логические операторы

x = 2
y = 3

res = x != y # оператор "не равно"

res = x == y # оператор "равно"

res = x < y # оператор "меньше"

res = x >= y # оператор "больше либо равно"

# print (f"\nРезультат: {res}")


z = True 
k = False 

# print ( not z ) # оператор НЕ (инвертирующий оператор)

# print ( not z and k  ) # оператор И ()

# print ( not z or k  ) # оператор ИЛИ

condition = z and (z or k) 


# print ( condition ) 

# условные операторы 

a = 5

if a >= 5:
    c = "больше или равно 5"
elif a == 4:
    c = "равно 4"
elif a == 3:
    c = "равно 3"
else:
    c = "Не равно 5"

# print (c)


# b = 11

# if b > 0 and < 10:
#     print("Лампочка ВКЛ")
# else:
#     print("Лампочка ВЫКЛ")

# ****Простой калькулятор****


num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

operation = input("Введите символ операции (+. -. *. /.): ")

if operation == "+": 
    res = num_1 + num_2
elif operation == "-":
    res = num_1 - num_2
elif operation == "*":
    res = num_1 * num_2
elif operation == "/":
    res = num_1 / num_2
else:
    res = "Введенный симвод некорректный!!!"



print(f"Результат: {res}")





