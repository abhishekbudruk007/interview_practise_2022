# str1 = "aaAbBBeEfgFFG"
# converted_string = str1.upper()
# print(converted_string)
# dict = {}
# count = 0
# for ch in converted_string:
#     print(dict.get(ch, ''))
    # break
    # if dict.get(ch):
    #     count += 1
    #     dict[ch] = count
    # else:
    #     count = 1
#     #     dict[ch] = count
# print(dict)
# for k,v in dict.items():
#     print(f"{k} is repeated {v} times")




# class A:
#     def __init__(self, name):
#         self.name = name
#     def display(self):
#         print(f'This is {self.name}')
#
# # class B(A):
# #     def display(self):
# #         print("This is class B")
#
# obj = A("Abhishek")
# obj.display()
#
# obj1 = A("TCS")
# obj1.display()

# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#
# class B(A):
#     def display(self):
#         print("This is class B")
#
#
# a = B()
# a.display()


# /endpoint

# json()

# POST and PUT


# select * from table_name

# select name from table_name

# select start from table_name where name = "Abhishek"

# insert into table_name ( name , age ) values ('abhishek', 29)
# import traceback
# try :
#      c = 10 / 0
# except Exception as e:
#     print(e)
#     print(traceback.print_exc())

#
# numbers = [1, 2, 3, 4]
# result = list(map(lambda x:x ** 2 , numbers))
# print(result)
#
#
# import  math
str1 = "aaAbBBeEfgFFG"
converted_string = str1.upper()
dict1 = { item + ":" +str(converted_string.count(item)) for item in set(converted_string)}
print(dict1)



a = {}
print(type(a))