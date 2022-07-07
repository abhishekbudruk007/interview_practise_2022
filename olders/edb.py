# a = 10
# b = 20
# print(a, b)


# monkey patching

def display():
    print("This is class A")

def validate(cls):
    def inner(*args, **kwargs):
        cls.display = display
        return cls
    return inner
@validate
class A:
    pass

obj=A()
print(obj.display())