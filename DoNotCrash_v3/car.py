from abc import ABC, abstractmethod


class Car(ABC):
    """ Abstract base class for car  """

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def steering(self):
        pass
