from abc import ABC, abstractmethod


class Car(ABC):
    """ Abstract class for car since I'm dealing with more than one car this will be a vital blueprint """

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def steering(self):
        pass
