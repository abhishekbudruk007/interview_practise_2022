
# def mathe(eq):
#     lhs = eval(eq.split("=")[0])
#     rhs = eq.split("=")[1]
#     print(lhs)
#     print(rhs)
#     rhs = lhs
#     if lhs == rhs:
#         print(rhs)
#
#
#
# eq = "3x + 12 = 46"
# mathe(eq)


# def StringChallenge(strParam):
#   print(strParam)
#   special_symbols = ['$', '@', '#', "%", "!"]
#   import pdb; pdb.set_trace()
#   if len(strParam) < 7 and len(strParam) > 32:
#     return False
#   elif not any(ch.isdigit() for ch in strParam):
#     return False
#   elif not any(ch.upper() for ch in strParam):
#     return False
#   elif not any(ch.lower() for ch in strParam):
#     return False
#   elif not any (ch in special_symbols for ch in strParam):
#     return False
#   elif "password" in strParam:
#     return False
#   else:
#     return True
#
# # keep this function call here
# print(StringChallenge("apple!M7"))



# def StringChallenge(strParam):
#   input = strParam.split()[0]
#   output = strParam.split()[1]
#   count_input = 0
#   for i in range(len(input)-1):
#     if input[i] == "$" or input[i] == "+":
#       count_input += 1
#     if input[i] == "*":
#       number = 3
#       if input[i+1] == "{":
#         number = int(input[i+2])
#       count_input += number
#   if len(output) == count_input:
#     return True
#   else:
#     return False
#
# # keep this function call here
# print(StringChallenge("$**+*{2} 9mmmrrrkbb"))


def get_result(a, b, operator):
  # import pdb;pdb.set_trace()
  if operator == "+":
    return a + b
  elif operator == "-":
    return a - b
  elif operator == "*":
    return a * b
  else:
    return a // b


def MathChallenge(strParam):
  eqauation = strParam.split()
  operand1 = eqauation[0]
  operator = eqauation[1]
  operand2 = eqauation[2]
  result = eqauation[-1]
  if 'x' in result:
    operand1 = int(operand1)
    operand2 = int(operand2)
    res = get_result(operand1, operand2, operator)
  else:
    if 'x' in operand1:
      x = operand1
      result = int(result)
      operand2 = int(operand2)
      if operator == "+":
        res = result - operand2
      elif operator == "-":
        res = result + operand2
      elif operator == "*":
        res = result // operand2
      else:
        res = result * operand2
      # res = get_result(operand1, operand2, operator)
    else:
      x = operand2
      result = int(result)
      operand2 = int(operand1)
      if operator == "+":
        res = result - operand2
      elif operator == "-":
        res = result + operand2
      elif operator == "*":
        res = result // operand2
      else:
        res = result * operand2
      # res = get_result(operand1, operand2, operator)
  res = str(res)
  # print(x)
  final_result = ''

  for i in range(len(x)):
    if x[i] == 'x':
      final_result = res[i]
      break
  # final_result = [res[i] for i in range(len(x)) if x[i] == 'x'][0]
  # print(final_result)
  return final_result

  # k = 0
  # # for i in x:
  # #   if i == 'x':
  # #     result = res[k]
  # #     break
  # #   else:
  # #     k = k + 1
  # return res


# keep this function call here
# print(MathChallenge("1x0 * 12 = 1200"))
# print(MathChallenge("3x + 12 = 46"))
print(MathChallenge("3 + 81x = 380"))
