from abc import ABC, abstractmethod


class Car(ABC):
    """ Abstract class for car since I'm dealing with more than one car this will be a vital blueprint """

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def getVelocity(self):
        pass

    @abstractmethod
    def getDirection(self):
        pass

    @abstractmethod
    def getPosition(self):
        pass

    @abstractmethod
    def calcTurningRad(self):
        pass

    @abstractmethod
    def turn(self):
        pass

    @abstractmethod
    def getSize(self):
        pass
