from abc import ABC, abstractmethod
class A(ABC):

    # def __init__(self):
    #     print("A")

    @abstractmethod
    def display(self):
        print("A")

class B(A):

    # def __init__(self):
    #     print("B")
    def display(self):
        print("B")


b= A()
b.display()
