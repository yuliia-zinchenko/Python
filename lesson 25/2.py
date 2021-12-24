class Human:
    def __init__(self,name,surname,age,place_of_birth,year_of_birth,n):
        self.name = name 
        self.surname = surname 
        self.age = age
        self.place_of_birth = place_of_birth
        self.year_of_birth = year_of_birth
        print(f"Name: {self.name}, Surname: {self.surname},Age: {self.age} Place of birth: {self.place_of_birth}, Year of birth :{self.year_of_birth}")
        print(f"Year:{n - int(self.year_of_birth)}")    
        
p1 = Human('Den','Dmitriev',24,'Ua',1997,2021)
p2 = Human('Tim','Pilipenko',16,'Ua',2005,2032)
p3 = Human('Artem','Dorogin',15,'Ua',2006,2064)
