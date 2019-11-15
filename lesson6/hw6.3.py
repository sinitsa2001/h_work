#Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
#surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self,name,surname,position,_income):
        self.name = name
        print(name)
        self.surname = surname
        print(surname)
        self.position = position
        print(position)
        self._income = _income
d = Worker_income = {"wage":10, 'bonus': 5}   # НЕ ПОНИМАЮ КАК ЭТО РЕАЛИЗОВАТЬ...ТУТ ВРОДЕ НЕ РУГАЕТСЯ..НО НЕ РАБОТАЕТ..!!!
print(Worker_income)
class position(Worker):

    def name_metod(self):
        print("Полное имя и фамилия работника ")
a = position(input("Введите имя: "), input('Введите фамилию: '), input("Введите должность: "), [1]+[9])
a.name_metod()





