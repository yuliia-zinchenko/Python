n = float(input('0- Rocket, 1- Car: '))
class Mashin:
    def __init__(self, mark, name, time, speed):
        self.mark = mark
        self.name = name
        self. time = time
        self.speed = speed
        print('Your choice:')
class  Rocket ( Machine ):
    def info(self):
        print(f'Model: {self.mark}')
        print(f'Name: {self.name}')
        print(f'Time: {self.time}')
        print(f'Speed: {self.speed}')
class  Car ( Machine ):
    def info_2(self):
        print(f'Model: {self.mark}')
        print(f'Name: {self.name}')
        print(f'Time: {self.time}')
        print(f'Speed: {self.speed}') 
if n == 0:
    flying_1  =  Rocket ( 'NASA' , 'rocket 3' , '3:30' , '15 km/s' )
    t = flying_1.info()
    print(t)
elif  n  ==  1 :
    flying_2 = Car('ford', 'name', '6:40', '90 km/h')
    t = flying_2.info_2()
    print(t)
