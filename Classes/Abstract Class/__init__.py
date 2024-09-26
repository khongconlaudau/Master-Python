from abc import ABC, abstractmethod

class Stream(ABC):
    @abstractmethod
    def read(self):
        pass

class Network(Stream):
    def read(self):
        print("Read from network")

class File(Stream):
    def read(self):
        print("Read from file")


file = File()