# Case study: Create a user management system for a system
# Constraints:
# 1. Known entities are User and User Group
# 2. User will be a member of User Group. User can be part of as many User Group as required
# 3. Within a User Group all member User will have exactly same permissions/access
# 4. User have an hierarchy or manager-to-reporter
# 5. The manager should automatically get the access to the User Group of reporters
# For example: User A i member of User Group 1 & 3, and User K is member of User Group 1 & 6
# and User P is member of User Group 16
# Now, both User A & User K have User P as manager,
# so User P should have access to User Group 1, 3, 6, and 16
# Objective:
# 1. List all tables and relationships to be created to maintain this
# 2. List all APIs that is actions to be created to manage this




# UserGroups
#  -> permissions
#
#
# User
#  -> user_group = ManyToMany(UserGroups)
#  -> Other Details of User
#
#











# weekdays = {10: 'sun', 12: 'mon', 6: 'fri', 7: 'sun', 9: 'mon', 8: 'mon', 3: 'tue', 4: 'wed', 5: 'thu'}
#
# keys = set(weekdays.keys())
# final_result= {}
# for k in keys:
#     if weekdays[k] not in final_result:
#         final_result[k] = weekdays[k]
# print(final_result)


#
# list_input = [12, 15, 20, "New Delhi", "India", 34, "Axtria" , 30.5]
# list_output_required = ["even", "odd", "even", "string", "string", "even", "string"]
# result_list = [ "string" if type(item) == str else "even" if (type(item) == int and item%2 == 0) else "odd" for item in list_input]
# print(result_list)
#
# map(lambda x: type(x), list_input)






