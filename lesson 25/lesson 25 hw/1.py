
class Countrys:
    def __init__(self,name,stolica,language,naselenie,valuta,chasovoi_poyas):
        self.name = name
        self.stolica = stolica
        self.language = language
        self.naselenie = naselenie
        self.valuta = valuta
        self.chasovoi_poyas = chasovoi_poyas
        print(f"Название страны: {self.name}\nСтолица страны: {self.stolica}\nЯзык: {self.language}\nНаселение страны: {self.naselenie}\nВалюта: {self.valuta}\nЧасовые поюса: {self.chasovoi_poyas}\n")
country_ukraine = Countrys('Украина','Киев','Украинский','41 723 998','UAH','UTC+1 — UTC+2')
country_rossia = Countrys('Россия','Москва','Русский','146 171 015','RUB','	UTC+2 — UTC+12')
country_poland = Countrys('Польша','Варшава','Польский','38 244 000','PLN','UTC+1 — UTC+2)')
country_germany = Countrys('Германия','Берлин','Немецкий','83 019 200','EUR','UTC+1 — UTC+2')
country_japan = Countrys('Япония','Токио','Японский','125 552 000','Японская Иена','JST')
country_usa = Countrys('США','Вашингтон','Английский','333 449 281','USD','UTC-5 — UTC-10')
country_dania = Countrys('Дания','Копенгаген','Датский','5 822 763','DKK','UTC+1 — UTC+2')
country_france = Countrys('Франция','Париж','Французкий','68 084 217','EUR','UTC+1 — UTC+2')
