"""
    Name: Byron Dowling
    Class: 4143 Programming Techniques
    Date: 11/08/2021

    Concepts:
        - OOP Python Concepts
        - pass
            - allows to declare class without initializing

    in-class
        - two classes
            - bike class
            - mountain bike class
        - essentially the same one from Java
"""

class Bicicyle:

    gear = int()
    speed = int()

    def __init__(self, g = None, s = None):

        if not g is None:
            self.gear = g

        ## Else, predefined value
        else:
            self.gear = 4
        
        if not s is None:
            self.speed = s

        ## Else, predefined value
        else:
            self.speed = 8

    def PrintFeatures(self):
        print("Bicycle is a", self.gear,"gear",self.speed, "speed")


    def Brake(self):
        print()
        print("Current speed is:", self.speed)
        self.speed = self.speed - 1
        print("Speed lowered to:", self.speed)


    def SpeedUp(self):
        print()
        print("Current speed is:", self.speed)
        self.speed = self.speed + 1
        print("Speed increased to:", self.speed)



## Class extending the Bicycle Class
class MountainBike(Bicicyle):

    seat_height = int()

    def __init__(self, g = None, s = None, sh = None):

        super().__init__(g, s)

        if not sh is None:
            self.seat_height = sh;

        else:
            self.seat_height = 12





object1 = Bicicyle(6, 10)
object2 = Bicicyle()

object1.PrintFeatures()
object2.PrintFeatures()

object3 = MountainBike(6, 10)
object4 = MountainBike()

object3.PrintFeatures()
object4.PrintFeatures()
object3.SpeedUp()
object4.Brake()