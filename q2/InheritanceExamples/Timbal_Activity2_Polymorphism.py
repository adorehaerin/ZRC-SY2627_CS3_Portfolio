#1. a. Duck typing is a way to achieve polymorphism without inheritance, 
#       where objects are treated based on whether they possess the required
#       attributes and methods, following the adage: "If it looks like a duck and quacks like a 
#       duck, it must be a duck" :)
    #b. It needed the minimum necessary attributes and methods, specifically a speak() method
#        and the alive attribute, that the loop expected.


#2.
#   a. define the classes
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

# b. define the start_trip function
def start_trip(vehicle):
    vehicle.move()

# c. create one object of each class
car = Car()
boat = Boat()
drone = Drone()

# d. call start_trip() for each object
start_trip(car)
start_trip(boat)
start_trip(drone)


# 3. The code demonstrates polymorphism through duck typing: the start_trip() function can 
#      accept any object (Car, Boat, or Drone) and call vehicle.move() successfully, simply
#       because every class shares the common move() interface rather than relying on a shared
#       parent class.

#hi sir >:3