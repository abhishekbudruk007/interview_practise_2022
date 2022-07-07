# Emps
# ---------------------------------------
# ID | Name | Manager
# ID |
# ---------------------------------------
# 1 | Eric | NULL |
# 2 | Jack | 1 |
# 3 | Viral | 2 |
# 4 | Michael | 2 |
# 5 | Nitesh | 1 |
# 6 | George | 4 |
# 7 | Ryan | 2 |
# .
# .
# .
#
# Emp == > {id: int, name: string, mid: int}
#
# Write
# a
# function...which
# takes
# input as a
# list
# of
# Emp(s), prints
# out
# the
# org
# chart as follows:
#
# Eric
# | __ Jack
#        | __Viral
#        | __Michael
#           | __George
#        | __Ryan
# | __ Nitesh


def create_dict(list_emp):
    levels = {}
    for obj in list_emp:
        if obj['mid'] != 'None':
            if obj['mid'] not in levels:
                levels[obj['mid']] = [obj]
            else:
                levels[obj['mid']].append(obj)
        else:
            levels[0] = [obj]
    return levels

# Emps
# ---------------------------------------
# ID | Name | Manager
# ID |
# ---------------------------------------
# 1 | Eric | NULL |
# 2 | Jack | 1 |
# 3 | Viral | 2 |
# 4 | Michael | 2 |
# 5 | Nitesh | 1 |
# 6 | George | 4 |
# 7 | Ryan | 2 |
# .
import json

list_emp = [{'id':'1','name':'Eric','mid':'None'},
            {'id':'2','name':'Jack','mid':'1'},
            {'id':'3','name':'Viral','mid':'2'},
            {'id':'4','name':'Michael','mid':'2'},
            {'id':'5','name':'Nitesh','mid':'1'},
            {'id':'6','name':'George','mid':'4'},
            {'id':'7','name':'Ryan','mid':'2'}
            ]

emp_dict = create_dict(list_emp)
print(json.dumps(emp_dict, indent = 3))
# def display_levels(emp_dict):
#     final_result
#     for k, v in emp_dict.items():
#         for obj in v:
#             result = {}
#             if obj['id'] in k:
#                 if "level_" +
#                     result["level_" + obj['id']] = obj['name']
#                 final_result.append(result)
#             if obj['id'] in k:
#                 print("_" + obj['name'])
#             print("\t |")


# levels = {
#     '0': [{'eric_id': 'Eric'}],
#     '1': [{Jack}, {Nitesh}],
#     '2': [{Viral}, {Michael}, {Ryan}],
#     '4': [{George}]
# }

# for mid, values in levels.items():
#     for eid, name in
#         print(name)
#
# list_emp = ["Eric", "jack", "Virael"]
#
#
# display_levels = display_levels(emp_dict)
# print(display_levels)


