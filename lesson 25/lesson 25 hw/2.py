class Cars:
    def __init__(self,name,country,data,osnovateli,type):
        self.name = name
        self.country = country
        self.data = data
        self.osnovateli = osnovateli
        self.type = type
        print(f"Название: {self.name}\nСтрана: {self.country}\nДата основания: {self.data}\nОснователи: {self.osnovateli}\nТип: {self.type}\n")
car_audi = Cars('Audi','Германия: Ингольштадт','1909','Август Хорьх ','Акционерное общество')
car_jaguar = Cars('Jaguar',' Великобритания: Ковентри','1922','Уильям Лайонс и Уильям Уолмсли','Частная компания')
car_merc = Cars('Mercedes-Benz','Германия: Штутгарт','1926','Карл Бенц, Готлиб Даймлер и Вильгельм Майбах','Подразделение Daimler AG')
car_astmart = Cars('Aston Martin','Великобритания: Гейдон','1913','Роберт Бэмфорд и Лайонел Мартин','Частная компания')
car_tesla = Cars('Tesla','Пало-Алто, Санта-Клара, Калифорния, США','2003','	Мартин Эберхард и Марк Тарпеннинг','Публичная компания')
car_bmw = Cars('BMW',' Германия: Мюнхен','1916','Карл Фридрих Рапп и Густав Отто','Акционерное общество')
