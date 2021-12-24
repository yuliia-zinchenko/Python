class Human:
    def info(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Place of birth: {self.place_of_birth}")
    def year(self,n):
        print(f"Year:{n - int(self.year_of_birth)}")    
p1 = Human()
p1.name = 'Den'
p1.surname = 'Dmintriev'
p1.place_of_birth = 'UA'
p1.year_of_birth = '1997'
p1.info()
p1.year(2021)
p2 = Human()
p2.name = 'Tim'
p2.surname = 'Pilipenko'
p2.place_of_birth = 'UA' 
p2.year_of_birth = '2005'
p2.info()
p2.year(2010)
p3 = Human()
p3.name = 'Tema'
p3.surname = 'Doroin'
p3.place_of_birth = 'UA' 
p3.year_of_birth = '2006'
p3.info()
p3.year(2103)
