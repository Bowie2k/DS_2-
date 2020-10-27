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

john = Human("John", 2)
john.move()
john.info() 