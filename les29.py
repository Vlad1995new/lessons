# Создайте класс на тему животных. В классе должен присутствовать конструктор не менее трёх методов.
class Animal:
    def __init__(self, name, age, who):
        self.name = name
        self.age = age
        self.who = who

    def otvet(self):
        if int(self.age[0:2]) >= 10:
            print(
                "Ваш, " + self.name + ", с Вами уже " + self.age + ". Советуем пройти бессплатный профилактический медосмотр в нашей клинике!")
        else:
            print(
                "Ваш, " + self.name + ", с Вами уже " + self.age + ". Советуем кормить 6 раз в день не большими порциями и выгуливать минимум 1 раз в день")


print("Укажите имя, возраст и происхождение вашего домашнего животного")
Animal1 = Animal("Кузя", "10 лет", "кот")
Animal1.otvet()
Animal1 = Animal("Тузик", "2 года", "собака")
Animal1.otvet()
