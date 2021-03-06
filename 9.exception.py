# *** Обработка исключений (исключительно события, искл. ситуации) ***


# генерация исключения 
a = 100
b = 0

# "деление на ноль" - пример ошибки (не рабочий код)
# c = a / b 


# решение - обработка исключений 
# конструкция "try-except"

# try:
#     # потенциальный аварийный код
#     c = a / b
#     print("Всё отлично")
# except:
#     # тут должен быть код, который срабатывает при исключительных ситуациях
#     # т.е. "запасной" код
#     print("Что-то пошло не так")
#     c = a / 0.1

# # тут может быть код который выполняется после предыдущего блока
# print("Result: ", c)


# Обработка множества исключений

# result = None

# try:
#     var = int(input("Введите число, но не ноль: "))
#     result = 50 / var
# # обработка исключения конкретного типа (класса) 
# # except ZeroDivisionError: # в данном примере тип исключения - ZeroDivisionError
# #     print("Вы попытались поделить на ноль!")
# #     result = 50 / 1
# # except ValueError as val_error: # в данном примере тип исключения - ValueError, его информация передается в val_error
# #     print(f"По-моему, Вы ввели не число. Инфо: {val_error}")
# #     result = 0


# # обработка общего (базового) исключения - он отлавливает все исключения
# except Exception as err:
#     pront(f"Что-то пошло не так:{err}")

# print("Result: ", result)

# конструкция "try-except-finally"

try:
    var = int(input("Введите число: "))
    c = 100 / var
    print("Полет нормальный!")
except ZeroDivisionError:
    c = 0 
    print("Попытка деления на ноль")
else:
    print("Логика, которая выполняется только если нет исключений")
finally:
    # finally срабатывает в любом случае, даже если программа завершается аварийно 
    # т.е. тут должна быть критически важная логика
    print("Критически важное действие")

print("Result", c)
