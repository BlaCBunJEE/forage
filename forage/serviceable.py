from abc import ABC, abstractmethod


class Serviceable(ABC):

    @abstractmethod
    def needs_service(self):
        pass

    @abstractmethod
    def tyre_needs_service(self):
        pass
