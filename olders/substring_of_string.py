def find_substring(s,n):
    if n <= 1:
        return s
    result_list = []
    substring_list = []
    for i in range(n):
        for j in range(i):
            sub_string = s[j:i]
            substring_list.append(sub_string)
    print(substring_list)
    result_list = [[ch for ch in sub_str] for sub_str in substring_list if len(sub_str) > 1]
    return result_list

s = "abcabcbb"
n = len(s)
print(find_substring(s, n))