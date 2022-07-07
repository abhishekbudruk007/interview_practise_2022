
def swap_values(function):
    def wrapper(*args, **kwargs):
        args= list(args)
        if args[0] < args[1]:
            args[0],args[1] = args[1], args[0]
        result = function(*args, **kwargs)
        return result
    return wrapper

@swap_values
def divide(a,b):
	return a/b


print(divide(30,10))






# swap the argument values. Write the decorator for the same?


# How many objects and reference variables are there for the given Python code?
#
# class Emp:
# 	print("Inside class")
# Emp()
# Emp()
# obj=Emp()

