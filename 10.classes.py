# **** Основы Объектно-ориентированного программирования (ООП) ****

# Объекты обладает свойствами и методами.
# Каждый объект принадлежит к определенному типу (классу).
# Класс - это "чертеж" объекта.
# "Реализация" класса - объект (экземпляр, инстанс).

# Создание класса. Название класса принято писать с заглавной буквы
class Cat(object):
	# метод (метод экземпляра) - функция внутри класса
	def mur(self, name):
		# атрибут (свойства, поля)
		self._name = name
		print("Мяу! Меня зовут: ", self._name)

	# метод инфо
	def info(self):
		print(f"Name: {self._name}")

# создание объекта (экземпляра) класса Cat
cat_1 = Cat()
cat_2 = Cat()

# вызов первого метода объекта
# cat_1.mur("Барсик")
# cat_2.mur("Гав")
# # вызов второго метода, который использует атрибут, созданным в первом методе
# cat_1.info()


# метод-конструктор
class Dog:
	# конструктор (initializer)
	# нужен для каких-либо настроек или других приготовлений 
	# в момент создания объектов
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight

	def gaf(self):
		print(f"Гав! Меня зовут {self.name}")

dog_1 = Dog("Цезарь", 10, 7.3)
dog_2 = Dog("Тузик", 5, 3.3)

# чтение значения атрибута
name_dog_1 = dog_1.name
# print(name_dog_1)
# изменение значения атрибута
dog_1.name = "Барбос"
# print(dog_1.name)
# print(name_dog_1)

# вызов метода
# dog_1.gaf()
# dog_2.gaf()


# *** Принцип Наследования - 1-й принцип ООП ***

# родительский (предковый) класс
class Animal:
	def __init__(self, legs=0):
		self.num_legs = legs
	
	def move(self):
		print(f"Я двигаюсь. У меня {self.num_legs} ног.")

# дочерние классы
class Insect(Animal):
	pass

class Wolf(Animal):
	pass

bug = Insect(8)
wolf = Wolf(4)

# bug.move()
# wolf.move()

class Human(Animal):
	def __init__(self, name, num_legs):
		self.num_legs = num_legs
		self.name = name

	def info(self):
		print(f"Я человек. Меня зовут {self.name}")

# john = Human("John", 2)
# john.move()
# john.info() 

# **** Полиморфизм ****

# поли + морф = разные формы чего-то одного (информ объекты)

# 1 вид. Разные классы могут обладать методами с одним именем, но с разной функциональностью 

# родительский класс
class A:
    def method_1(self, arg):
        print(f'Data: {arg}')

# дочерний класс у которого родительский метод переопределен 
class A_1(A):
    def method_1(self, a, b):
        print(f"Data: {a + b}")

# создание экземпляров классов
a = A()
a_1 = A_1()

# вызов методов у экземпляров 
# a.method_1(100)
# a_1.method_1(10,20)

# * 2 вид. применение "магических" методов (методов перезагрузки операторов)

# метод, который позволяет из экземпляра (объекта) класса "делать" функцию 
class CustomSum:
    def __init__(self, param):
        self.coeff = param

    # маг-метод представляющий поведение обычной функции
    def __call__(self, a, b):
        res = (a + b) * self.coeff
        print(f"Result: {res}")

    # маг-метод
    def __str__(self):
        return f"Custom Summator. Coeff: {self.coeff}"

sum_1 = CustomSum(0.5)
sum_2 = CustomSum(1.53)

# эффект нашего "магического" метода 
# sum_1(2, 3)
# sum_2(2, 3) 

# print(sum_1)

# **** Инкапсуляция ****
# инкапсуляция - скрытие атрибутов и/или методов





class B:
    def __init__(self, arg):
        # не строго инкапсулированный атрибут
        self._attr = arg

        # "строго" инкапсулированный атрибут
        self._attr2 = 100

    # не строго инкапсулированный атрибут
    def _method(self):
        print("Hello!")

     # "строго" инкапсулированный атрибут
    def _method_2(self):
        print("World!")

b = B(100)
# print(b._attr)
# b._method()

# print(b._attr)
print(b._B__attr2)
# b.__method_2()
# b.method_3()


# **** Композиция (Агрегация) ****

# использование экземпляров одних классов внутри других классов

class C:
    def __call__(self, a):
        return a ** 2

class D:
    def method(self, x):
        c = C() # создается объект класса D
        return c(x) + x # используется в качестве функции 
        print(res)

d = D()
# d.method(10)