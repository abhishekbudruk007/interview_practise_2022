
def find_substring(s, n):
    if len(s) < 1:
        return 0
    substring = ''
    maxlen = 1
    for i in s:
        if i not in substring:
            substring += i
            maxlen = max(maxlen, len(substring))
        else:
            substring = substring.split(i)[1] + i
    return maxlen


s = "pwwkew"
# s = "abcabcbb"
n = len(s)

print(find_substring(s, n))