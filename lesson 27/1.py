a = int(input('Year of enter: '))
b = int(input('Year of graduat.:'))
c = b-a
class Human:
    def __init__ (self, name, surname, age, country, now, last, years_stud):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.now = now
        self.last = last
        self.years_stud = years_stud
        print('Human creation:')
    def info (self):
        print(f'Name: {self.name};')
        print(f'Surname: {self.surname};')
        print(f'Age: {self.age};')
        print(f'Country: {self.country};')
        print(f'Study in KPL')
        print(f'Year of enter:: {self.now};')
        print(f'Year of graduat.:: {self.last};')
        print(f'Total:: {self.years_stud};')        
        
Iliya = Human('Iliya', 'Yushenko', 16, 'UA', a, b, c)
t = Iliya.info()
print(t)
