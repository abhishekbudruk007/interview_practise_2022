#
#
#
#
# def dec(func):
#     def wrapper(*args, **kwargs):
#         result = hi()
#         return result.upper()
#
# @dec
# def hi():
#     return "hello"
#
#
# print(hi)


#
# def generator_example():
#     arr = range(1, 5)
#     for i in arr:
#         yield i
#
# gen_obj = generator_example()
# for i in range(1,5):
#     print(gen_obj.__next__())




def dec(function):
    def wrapper(*args, **kwargs):
        result = function()
        return result.upper()
    return wrapper

@dec
def hi():
	return "hello"


print(hi())










