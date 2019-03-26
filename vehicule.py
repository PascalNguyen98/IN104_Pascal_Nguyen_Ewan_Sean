class Vehicle:
    def __init__(self,brand,nb_seat,nb_door,color):
        self.brand=brand
        self.nb_seat=nb_seat
        self.nb_door=nb_door
        self.color=color
        
    def getBrand(self):
        return self.brand
    
    def getNb_seat(self):
        return self.nb_seat
        
    def getColor(self):
        return self.color
    def getNb_door(self):
        return self.nb_door
    
    

class Car(Vehicle):
    def __init__(self,brand,nb_seat,nb_door,color,horsepower,max_speed):
        self.horsepower=horsepower
        self.max_speed=max_speed
    def __str__(self):
        print( " i am a"+str(self.getColor(self))+ str(self.getBrand(self))+ "car.")
        
    
        
    def tuning(self,nb_horsepower):
        self.horsepower+=nb_horsepower
    
    def fly(self):
         print (" i cannot fly i'm a car")
    
    


class Helicopter(Vehicle):
    def __init__(self,brand,nb_seat,nb_door,color,fuel_tank,nb_blade):
        Vehicle.__init__(self,brand,nb_seat,nb_door,color)
        self.fuel_tank=fuel_tank
        self.nb_blade=nb_blade
    def getNb_blade(self):
        return self.nb_blade
    def __str__(self):
       print(" i am a "+str(self.getColor())+ " "+str(self.getBrand())+ " helicopter with "+ str(self.getNb_blade()) + " blades")
       
    def fly(self):
        print( " i believe i can fly")
        
vehicle=Vehicle("mercedes",4,2,"black")
car=Car("ferrari",4,2,"red",220,180)
heli=Helicopter("Airbus",4,2,"blue",250,5)
heli.__str__()    
heli.fly()
car.fly()
car.tuning(20)
print(car.horsepower)
